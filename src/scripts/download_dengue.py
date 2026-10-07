#!/usr/bin/env python3
"""
Pipeline de download e consolidação de dados de Dengue (SINAN/DATASUS)
Conversão do script R original para Python.

Equivalência de pacotes:
    R                             -> Python
    -----------------------------------------------------------------
    downloader / RCurl            -> ftplib (download via FTP do DATASUS)
    data.table::fread             -> pandas.read_csv(sep="\\t")
    read.dbc::dbc2dbf             -> pyreaddbc.dbc2dbf()   (.dbc -> .dbf)
    foreign::read.dbf             -> dbfread.DBF           (.dbf -> DataFrame,
                                     depois salvo como .tsv na seção 3)
    openxlsx / readxl             -> pandas.read_excel
    lubridate                     -> pandas.to_datetime
    dplyr / tidyverse             -> pandas (groupby, merge, assign, etc.)
    ribge::populacao_municipios   -> NÃO existe equivalente Python direto.
                                     Ver nota na seção "POPULAÇÃO" abaixo.
    readRDS (objeto sf)           -> pyreadr.read_r() + drop da coluna de
                                     geometria (só precisamos dos atributos)
    here::here                    -> pathlib

Pacotes Python necessários:
    pip install pandas numpy pyreaddbc dbfread openpyxl pyreadr xlrd

NOTA IMPORTANTE sobre os bugs corrigidos durante a conversão do R original:
  - City (código do município, 6 dígitos) precisa ser casado com
    `cod_munic6` (não `cod_municipio`, que tem 7 dígitos) em pop2024.
  - State precisa estar numérico para casar com `code_state` (double) em
    `estado`.
  - Os dois merges finais (pop2024 e estado) são passos independentes —
    cada um corrige um par de colunas diferente.
"""

import os
import re
import gc
import csv
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from ftplib import FTP

import numpy as np
import pandas as pd
import pyreadr
from dbfread import DBF
from pyreaddbc import dbc2dbf

# ========== 1. CONFIGURAÇÕES INICIAIS ==========
BASE_DIR = Path(__file__).resolve().parent
DIR      = BASE_DIR / "app" / "input"
B_FIN    = DIR / "finais"
B_PAR    = DIR / "parciais"
DIR_TSV  = DIR / "tsv"
DIR_TMP  = DIR / "tmp"   # .dbf e .tsv.part intermediários

for d in (B_FIN, B_PAR, DIR_TSV, DIR_TMP):
    d.mkdir(parents=True, exist_ok=True)

# Arquivos de apoio que precisam estar em DIR (copiados do projeto em R)
INSUMOS = [
    "sinan_calendario.txt",
    "pop2024.csv",
    "regioes_geograficas_composicao_por_municipios_2017_20180911.xls",
    "estados.rds",
]
ausentes = [n for n in INSUMOS if not (DIR / n).exists()]
if ausentes:
    raise SystemExit(f"Faltam arquivos em {DIR}:\n  " + "\n  ".join(ausentes))

SUF    = "DENG"
MYPATH = B_FIN  # substituir por B_PAR quando precisar trabalhar com dados preliminares

print("BASE_DIR:", BASE_DIR)
print("mypath:", MYPATH)

FTP_HOST = "ftp.datasus.gov.br"
FTP_DIR = (
    "/dissemin/publicos/SINAN/DADOS/FINAIS/"
    if MYPATH == B_FIN
    else "/dissemin/publicos/SINAN/DADOS/PRELIM/"
)


def listar_arquivos_ftp(diretorio: str, host: str = FTP_HOST) -> list[str]:
    ftp = FTP(host)
    ftp.set_pasv(False)   # importante para o DATASUS
    ftp.login()           # login anônimo sem argumentos
    ftp.cwd(diretorio)
    arquivos = ftp.nlst()
    ftp.quit()
    return arquivos


def baixar_arquivo_ftp(diretorio: str, nome_arquivo: str, destino: Path,
                       host: str = FTP_HOST) -> None:
    ftp = FTP(host)
    ftp.set_pasv(False)   # importante para o DATASUS
    ftp.login()           # login anônimo sem argumentos
    ftp.cwd(diretorio)
    with open(destino, "wb") as f:
        ftp.retrbinary(f"RETR {nome_arquivo}", f.write)
    ftp.quit()


try:
    filenames = listar_arquivos_ftp(FTP_DIR)
except Exception as e:
    print("Não foi possível acessar o FTP do DATASUS:", e)
    filenames = []

filenames = [f for f in filenames if SUF in f]

# ========== 2. VERIFICA O QUE JÁ EXISTE EM MYPATH ==========
fil = [f for f in os.listdir(MYPATH) if f.startswith(SUF)]
ja_baixados = set(fil)
faltando = [f for f in filenames if f not in ja_baixados]

print("-" * 74)
print(f"Aviso: Existem {len(filenames)} arquivos no sitio pesquisado")
print(f"Aviso: Existem {len(faltando)} arquivos para atualizar")
print("-" * 74)

for nome in faltando:
    print("Baixando:", nome)
    baixar_arquivo_ftp(FTP_DIR, nome, MYPATH / nome)

# ========== 3. CONVERSÃO .dbc -> .tsv (em paralelo) ==========
ANO_MIN_CONVERSAO = 13                      # use 0 para converter todos os anos
N_PROCESSOS = min(8, os.cpu_count() or 1)   # um arquivo por processo


def converter_dbc(file_base: str):
    """Converte um .dbc em .tsv. Devolve (nome, n_linhas, erro)."""
    dbc_path = MYPATH / f"{file_base}.dbc"
    dbf_path = DIR_TMP / f"{file_base}.dbf"
    part_path = DIR_TMP / f"{file_base}.tsv.part"
    tsv_path = DIR_TSV / f"{file_base}.tsv"
    try:
        dbc2dbf(str(dbc_path), str(dbf_path))
        tabela = DBF(str(dbf_path), encoding="latin1", load=False,
                     ignore_missing_memofile=True, char_decode_errors="replace")
        n = 0
        with open(part_path, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(tabela.field_names)
            for rec in tabela:          # streaming: não carrega o arquivo na RAM
                w.writerow(rec.values())
                n += 1
        part_path.replace(tsv_path)     # só aparece como .tsv se terminou inteiro
        return file_base, n, None
    except Exception as e:
        return file_base, None, str(e)
    finally:
        for tmp in (dbf_path, part_path):
            if tmp.exists():
                tmp.unlink()


files_dbc = [f for f in os.listdir(MYPATH) if f.lower().endswith(".dbc")]
files_tsv_existentes = [f[:-4] for f in os.listdir(DIR_TSV) if f.endswith(".tsv")]

pendentes = sorted(set(f[:-4] for f in files_dbc) - set(files_tsv_existentes))
pendentes = [p for p in pendentes if int(re.search(r"\d+", p).group()) >= ANO_MIN_CONVERSAO]
# maiores primeiro, para os processos terminarem mais ou menos juntos
pendentes.sort(key=lambda p: (MYPATH / f"{p}.dbc").stat().st_size, reverse=True)

print("Arquivos pendentes de conversão:", len(pendentes))
print(sorted(pendentes))

if pendentes:
    ctx = mp.get_context("fork")
    with ProcessPoolExecutor(max_workers=N_PROCESSOS, mp_context=ctx) as ex:
        futuros = [ex.submit(converter_dbc, p) for p in pendentes]
        for fut in as_completed(futuros):
            nome, n, erro = fut.result()
            if erro:
                print("ERRO em", nome, ":", erro)
            else:
                print(nome, "ok -", n, "linhas")

# ========== 4. CONSOLIDAÇÃO POR SEMANA EPIDEMIOLÓGICA (SINAN) ==========
# Roda duas vezes em sequência (equivale ao `repeat` com AUX do script em R):
#   1ª passada: somente casos CONFIRMADOS  -> *_CONFIRMADOS_dash_new.tsv
#   2ª passada: todos os casos NOTIFICADOS -> *_NOTIFICADOS_dash_new.tsv
INCLUIR_EVOLUCAO = True   # o script em R também agrega por EVOLUCAO

myfiles = sorted(f for f in os.listdir(DIR_TSV) if f.startswith(SUF) and f.endswith(".tsv"))
anos = [int(re.search(r"\d+", f).group()) for f in myfiles]
myfiles = [f for f, a in zip(myfiles, anos) if a >= 13]

calendario = pd.read_csv(DIR / "sinan_calendario.txt", sep="\t")
# ajuste o separador acima se o arquivo original usar vírgula em vez de tab

RACE_MAP = {1: "Branca", 2: "Preta", 3: "Amarela", 4: "Parda", 5: "Indigena", 9: "Ignorado"}


def calc_idade_padrao(age_temp) -> float:
    s = str(age_temp)
    if len(s) == 2:
        return float(s)
    if s[:2] == "40":
        return float(s[2:4])
    return 0.0


def para_int(serie: pd.Series) -> pd.Series:
    """Converte para inteiro anulável, para os merges não brigarem por tipo."""
    return pd.to_numeric(serie, errors="coerce").astype("Int64")


# ---- dados de apoio (carregados uma única vez, usados nas duas passadas) ----
# POPULAÇÃO: não existe pacote Python equivalente ao `ribge`. Rode no R, uma vez:
#   write.csv(ribge::populacao_municipios(2024), "pop2024.csv", row.names = FALSE)
pop2024 = pd.read_csv(DIR / "pop2024.csv", sep="\t", dtype={"cod_municipio": str, "cod_munic6": str})

meso_regiao = pd.read_excel(
    DIR / "regioes_geograficas_composicao_por_municipios_2017_20180911.xls",
    dtype={"CD_GEOCODI": str},
)
meso_regiao_pop = pop2024.merge(
    meso_regiao, left_on="cod_municipio", right_on="CD_GEOCODI", how="left"
)
meso_regiao_pop["codigo_uf"] = para_int(meso_regiao_pop["codigo_uf"])
meso_regiao_pop["cod_munic6"] = para_int(meso_regiao_pop["cod_munic6"])

# estados.rds (objeto sf) -> pyreadr devolve um dict {nome_objeto: DataFrame}
import pandas as pd  
estados_result = pd.read_csv(DIR / "estados.csv")
estado = estados_result

if "geometry" in estado.columns:
    estado = estado.drop(columns=["geometry"])
estado = estado[["code_state", "abbrev_state", "name_state", "name_region"]].copy()
estado["code_state"] = para_int(estado["code_state"])


def consolidar(confirmados: bool) -> None:
    rotulo = "CONFIRMADOS" if confirmados else "NOTIFICADOS"
    print("=" * 74)
    print("Consolidando:", rotulo)
    print("=" * 74)

    lista = []
    for f in myfiles:
        print("Arquivo:", f)
        temp_file = pd.read_csv(DIR_TSV / f, sep="\t", low_memory=False)

        ano_calend = "20" + re.sub(r"[^0-9]", "", f)
        cale_year = calendario[calendario["ANO"].astype(str) == ano_calend]

        temp_file["DT_NOTIFIC"] = pd.to_datetime(temp_file["DT_NOTIFIC"])
        temp_file["weekStart"] = pd.NaT

        for _, row in cale_year.iterrows():
            inicio = pd.to_datetime(row["Início"])
            fim = pd.to_datetime(row["Término"])
            mask = (temp_file["DT_NOTIFIC"] >= inicio) & (temp_file["DT_NOTIFIC"] <= fim)
            temp_file.loc[mask, "SEM_NOT"] = row["SEM_NOT"]
            temp_file.loc[mask, "weekStart"] = inicio

        if confirmados:
            temp = temp_file[
                (temp_file["CRITERIO"] < 3)
                & (temp_file["CLASSI_FIN"] >= 10)
                & (temp_file["CLASSI_FIN"] <= 12)
            ].copy()
        else:
            temp = temp_file.copy()

        group_cols = ["DT_NOTIFIC", "SEM_NOT", "weekStart", "SG_UF_NOT",
                      "ID_MUNICIP", "NU_IDADE_N", "CS_SEXO", "CS_RACA"]
        nomes = ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
                 "Age_temp", "Sex", "Race_Colour"]
        if INCLUIR_EVOLUCAO:
            group_cols.append("EVOLUCAO")
            nomes.append("EVOLUCAO")
        nomes.append("New_Cases")   # a coluna agregada vem sempre por último

        if "total" in temp.columns:
            temp_agre = (
                temp.groupby(group_cols, as_index=False)["total"]
                .sum()
                .rename(columns={"total": "new_cases"})
                .dropna()
            )
        else:
            temp_agre = (
                temp.groupby(group_cols, as_index=False)
                .size()
                .rename(columns={"size": "new_cases"})
                .dropna()
            )

        temp_agre.columns = nomes
        temp_agre["Noti_Date"] = pd.to_datetime(temp_agre["Noti_Date"])
        temp_agre["Race_Colour"] = temp_agre["Race_Colour"].map(RACE_MAP)
        temp_agre["Age"] = temp_agre["Age_temp"].apply(calc_idade_padrao)

        colunas = ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
                   "New_Cases", "Age", "Sex", "Race_Colour"]
        if INCLUIR_EVOLUCAO:
            colunas.append("EVOLUCAO")
        temp_agre_final = temp_agre[colunas].copy()

        temp_agre_final["City"] = para_int(temp_agre_final["City"])
        temp_agre_final["Noti_Week"] = para_int(temp_agre_final["Noti_Week"])

        lista.append(temp_agre_final)
        del temp_file, temp, temp_agre, temp_agre_final
        gc.collect()

    novo = pd.concat(lista, ignore_index=True)
    novo["State"] = para_int(novo["State"])

    base_final = novo.merge(
        meso_regiao_pop,
        left_on=["State", "City"],
        right_on=["codigo_uf", "cod_munic6"],
        how="left",
    )
    base_final = base_final.merge(
        estado, left_on="State", right_on="code_state", how="left",
    )

    out_name = f"2014-2025_DENGUE_{rotulo}_dash_new.tsv"
    base_final.to_csv(DIR / out_name, sep="\t", index=False)
    print("Gravado:", DIR / out_name, f"({len(base_final)} linhas)")

    del lista, novo, base_final
    gc.collect()


for confirmados in (True, False):
    consolidar(confirmados)

