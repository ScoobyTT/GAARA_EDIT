#!/usr/bin/env python3
"""
Pipeline de download e consolidação de dados de Dengue (SINAN/DATASUS)
Conversão do script R original para Python.

Equivalência de pacotes:
    R                             -> Python
    -----------------------------------------------------------------
    downloader / RCurl            -> ftplib (download via FTP do DATASUS)""" 
#    data.table::fread             -> pandas.read_csv(sep="\\t")
"""    read.dbc::dbc2dbf              -> pyreaddbc.read_dbc()  (lê o .dbc direto
                                       para DataFrame; não precisamos mais do
                                       passo intermediário .dbf)
    foreign::read.dbf             -> não usado mais; trabalhamos direto com
                                       os .tsv gerados na seção 3
    openxlsx / readxl             -> pandas.read_excel
    lubridate                     -> pandas.to_datetime
    dplyr / tidyverse             -> pandas (groupby, merge, assign, etc.)
    ribge::populacao_municipios   -> NÃO existe equivalente Python direto.
    """
     #                                  Ver nota na seção "POPULAÇÃO" abaixo.
"""
    readRDS (objeto sf)           -> pyreadr.read_r() + drop da coluna de
                                       geometria (só precisamos dos atributos)
    here::here                    -> pathlib

Pacotes Python necessários:
    pip install pandas numpy pyreaddbc openpyxl pyreadr

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
from pathlib import Path
from ftplib import FTP

import numpy as np
import pandas as pd
import pyreaddbc
import pyreadr

# ========== 1. CONFIGURAÇÕES INICIAIS ==========
BASE_DIR = Path(__file__).resolve().parent
DIR      = BASE_DIR / "app" / "input"
B_FIN    = DIR / "finais"
B_PAR    = DIR / "parciais"
DIR_TSV  = DIR / "tsv"

for d in (B_FIN, B_PAR, DIR_TSV):
  d.mkdir(parents=True, exist_ok=True)

SUF    = "DENG"
MYPATH = B_FIN  # subistituir para " B_PAR " qnd precisar trabalhar com dados preliminares

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
    ftp.set_pasv(False)   #  importante para o DATASUS
    ftp.login()           #  login anônimo sem argumentos
    ftp.cwd(diretorio)
    arquivos = ftp.nlst()
    ftp.quit()
    return arquivos#!/usr/bin/env python3
"""
Pipeline de download e consolidação de dados de Dengue (SINAN/DATASUS)
Conversão do script R original para Python.

Equivalência de pacotes:
    R                             -> Python
    -----------------------------------------------------------------
    downloader / RCurl            -> ftplib (download via FTP do DATASUS)
    data.table::fread             -> pandas.read_csv(sep="\\t")
    read.dbc::dbc2dbf             -> pyreaddbc.read_dbc()  (lê o .dbc direto
                                     para DataFrame; não precisamos mais do
                                     passo intermediário .dbf)
    foreign::read.dbf             -> não usado mais; trabalhamos direto com
                                     os .tsv gerados na seção 3
    openxlsx / readxl             -> pandas.read_excel
    lubridate                     -> pandas.to_datetime
    dplyr / tidyverse             -> pandas (groupby, merge, assign, etc.)
    ribge::populacao_municipios   -> NÃO existe equivalente Python direto.
                                     Ver nota na seção "POPULAÇÃO" abaixo.
    readRDS (objeto sf)           -> pyreadr.read_r() + drop da coluna de
                                     geometria (só precisamos dos atributos)
    here::here                    -> pathlib

Pacotes Python necessários:
    pip install pandas numpy pyreaddbc openpyxl pyreadr xlrd

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
from pathlib import Path
from ftplib import FTP

import numpy as np
import pandas as pd
import pyreaddbc
import pyreadr

# ========== 1. CONFIGURAÇÕES INICIAIS ==========
BASE_DIR = Path(__file__).resolve().parent
DIR      = BASE_DIR / "app" / "input"
B_FIN    = DIR / "finais"
B_PAR    = DIR / "parciais"
DIR_TSV  = DIR / "tsv"

for d in (B_FIN, B_PAR, DIR_TSV):
    d.mkdir(parents=True, exist_ok=True)

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

# ========== 3. CONVERSÃO .dbc -> .tsv ==========
files_dbc = [f for f in os.listdir(MYPATH) if f.lower().endswith(".dbc")]
files_tsv_existentes = [f.replace(".tsv", "") for f in os.listdir(DIR_TSV)]

pendentes = sorted(
    set(f[:-4] for f in files_dbc) - set(files_tsv_existentes)
)

print("Arquivos pendentes de conversão:", len(pendentes))
print(pendentes)

for file_base in pendentes:
    dbc_path = MYPATH / f"{file_base}.dbc"
    tsv_path = DIR_TSV / f"{file_base}.tsv"
    try:
        base = pyreaddbc.read_dbc(str(dbc_path), encoding="latin1")
        base.to_csv(tsv_path, sep="\t", index=False)
        print(file_base, "ok -")
    except Exception as e:
        print("ERRO em", file_base, ":", e)

# ========== 4. CONSOLIDAÇÃO POR SEMANA EPIDEMIOLÓGICA (BAHIA / SINAN) ==========
myfiles = sorted(f for f in os.listdir(DIR_TSV) if f.startswith(SUF))
anos = [int(re.search(r"\d+", f).group()) for f in myfiles]
myfiles = [f for f, a in zip(myfiles, anos) if a >= 13]

calendario = pd.read_csv(DIR / "sinan_calendario.txt", sep="\t")
# ajuste o separador acima se o arquivo original usar vírgula em vez de tab

confirmados = True
lista_bahia = []

leve     = {1, 6, 10}
moderada = {2, 7, 11}
grave    = {3, 4, 8, 12}

RACE_MAP = {1: "Branca", 2: "Preta", 3: "Amarela", 4: "Parda", 5: "Indigena", 9: "Ignorado"}


def calc_idade_padrao(age_temp) -> float:
    s = str(age_temp)
    if len(s) == 2:
        return float(s)
    if s[:2] == "40":
        return float(s[2:4])
    return 0.0


def calc_idade_alt(age_temp) -> float:
    s = str(age_temp)
    if s[:1] in ("M", "D", "I"):
        return 0.0
    if s[:1] == "A":
        return float(s[1:4])
    if len(s) == 2:
        return float(s)
    return float(s[2:4])


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

    temp_agre.columns = ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
                         "Age_temp", "Sex", "Race_Colour", "New_Cases"]

    temp_agre["Noti_Date"] = pd.to_datetime(temp_agre["Noti_Date"])
    temp_agre["Race_Colour"] = temp_agre["Race_Colour"].map(RACE_MAP)
    temp_agre["Age"] = temp_agre["Age_temp"].apply(calc_idade_padrao)

    temp_agre_final = temp_agre[
        ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
         "New_Cases", "Age", "Sex", "Race_Colour"]
    ].copy()

    temp_agre_final["City"] = pd.to_numeric(temp_agre_final["City"], errors="coerce")
    temp_agre_final["Noti_Week"] = temp_agre_final["Noti_Week"].astype("Int64")

    lista_bahia.append(temp_agre_final)
    del temp_file, temp, temp_agre, temp_agre_final
    gc.collect()

newBahia = pd.concat(lista_bahia, ignore_index=True)
newBahia["State"] = pd.to_numeric(newBahia["State"])

# ========== POPULAÇÃO (equivalente a ribge::populacao_municipios(2024)) ==========
# Não existe pacote Python equivalente ao `ribge`. Solução:
# rodar no R `write.csv(pop2024, "pop2024.csv", row.names = FALSE)` uma
# vez e carregar esse CSV aqui.
pop2024 = pd.read_csv(
    DIR / "pop2024.csv",
    dtype={"cod_municipio": str, "cod_munic6": str},
)

meso_regiao = pd.read_excel(
    DIR / "regioes_geograficas_composicao_por_municipios_2017_20180911.xls"
)

meso_regiao_pop = pop2024.merge(
    meso_regiao, left_on="cod_municipio", right_on="CD_GEOCODI", how="left"
)

baseFinal = newBahia.merge(
    meso_regiao_pop,
    left_on=["State", "City"],
    right_on=["codigo_uf", "cod_munic6"],
    how="left",
)

# estados.rds (objeto sf) -> pyreadr devolve um dict {nome_objeto: DataFrame}
estados_result = pyreadr.read_r(str(DIR / "estados.rds"))
estado = next(iter(estados_result.values()))
if "geometry" in estado.columns:
    estado = estado.drop(columns=["geometry"])

baseFinal = baseFinal.merge(
    estado[["code_state", "abbrev_state", "name_state", "name_region"]],
    left_on="State", right_on="code_state", how="left",
)

out_name = (
    "2014-2025_DENGUE_CONFIRMADOS_dash_new.tsv"
    if confirmados else
    "2014-2025_DENGUE_NOTIFICADOS_dash_new.tsv"
)
baseFinal.to_csv(DIR / out_name, sep="\t", index=False)

del newBahia, baseFinal, meso_regiao, meso_regiao_pop
gc.collect()

# ========== "PARA ZE": granularidade diária, sem semana epidemiológica ==========
arquivos_tsv = sorted(f for f in os.listdir(DIR_TSV) if f.startswith(SUF))
anos = [int(re.search(r"\d+", f).group()) for f in arquivos_tsv]
t = [f for f, a in zip(arquivos_tsv, anos) if a >= 13]

confirmados = False
lista_newData = []

COLS_ZE = {
    "DT_NOTIFIC", "SEM_NOT", "SG_UF_NOT", "ID_MUNICIP",
    "NU_IDADE_N", "CS_SEXO", "CS_RACA", "CLASSI_FIN", "CRITERIO",
    "CON_CLASSI", "CON_CRITER", "NU_IDADE", "total",
}

for f in t:
    print(f)
    base = pd.read_csv(
        DIR_TSV / f, sep="\t", low_memory=False,
        usecols=lambda c: c in COLS_ZE,
    )

    rename_map = {}
    if "CON_CLASSI" in base.columns:
        rename_map["CON_CLASSI"] = "CLASSI_FIN"
    if "CON_CRITER" in base.columns:
        rename_map["CON_CRITER"] = "CRITERIO"
    idade_alt = "NU_IDADE" in base.columns
    if idade_alt:
        rename_map["NU_IDADE"] = "NU_IDADE_N"
    base = base.rename(columns=rename_map)

    base["Dengue_class"] = pd.NA
    base.loc[base["CLASSI_FIN"].isin(leve), "Dengue_class"] = "1"
    base.loc[base["CLASSI_FIN"].isin(moderada), "Dengue_class"] = "2"
    base.loc[base["CLASSI_FIN"].isin(grave), "Dengue_class"] = "3"

    if confirmados:
        base_temp = base[(base["CRITERIO"] < 3) & base["Dengue_class"].notna()].copy()
    else:
        base_temp = base.copy()

    base_temp["Noti_Year"] = int("20" + re.sub(r"[^0-9]", "", f))

    group_cols = ["DT_NOTIFIC", "SEM_NOT", "Noti_Year", "SG_UF_NOT",
                  "ID_MUNICIP", "NU_IDADE_N", "CS_SEXO", "CS_RACA"]

    if "total" in base_temp.columns:
        temp_agre = (
            base_temp.groupby(group_cols, as_index=False)["total"]
            .sum()
            .rename(columns={"total": "new_cases"})
            .dropna()
        )
    else:
        temp_agre = (
            base_temp.groupby(group_cols, as_index=False)
            .size()
            .rename(columns={"size": "new_cases"})
            .dropna()
        )

    temp_agre.columns = ["Noti_Date", "Noti_Week", "Noti_Year", "State", "City",
                         "Age_temp", "Sex", "Race_Colour", "New_Cases"]
    temp_agre["Noti_Date"] = pd.to_datetime(temp_agre["Noti_Date"])
    temp_agre["Race_Colour"] = temp_agre["Race_Colour"].map(RACE_MAP)
    temp_agre["Age"] = temp_agre["Age_temp"].apply(
        calc_idade_alt if idade_alt else calc_idade_padrao
    )

    temp_agre_final = temp_agre[
        ["Noti_Date", "Noti_Week", "Noti_Year", "State", "City",
         "New_Cases", "Age", "Sex", "Race_Colour"]
    ].copy()
    temp_agre_final["City"] = pd.to_numeric(temp_agre_final["City"], errors="coerce")

    lista_newData.append(temp_agre_final)
    del base, base_temp, temp_agre, temp_agre_final
    gc.collect()

newData = pd.concat(lista_newData, ignore_index=True)

# --- joins finais: cada um resolve um par de colunas de tipos diferentes ---
# 1) City (6 dígitos) <-> cod_munic6 (não cod_municipio, que tem 7 dígitos)
newData["City"] = newData["City"].astype("Int64").astype(str)
pop2024["cod_munic6"] = pop2024["cod_munic6"].astype(str)
newData = newData.merge(pop2024, left_on="City", right_on="cod_munic6", how="left")

# 2) State (numérico) <-> code_state
newData["State"] = pd.to_numeric(newData["State"])
newData = newData.merge(
    estado[["code_state", "abbrev_state", "name_state", "name_region"]],
    left_on="State", right_on="code_state", how="left",
)

out_name = (
    "2000-2025_DENGUE_CONFIRMADOS_new_ze.tsv"
    if confirmados else
    "2000-2025_DENGUE_NOTIFICADOS_new_ze.tsv"
)
newData.to_csv(DIR / out_name, sep="\t", index=False)

# pop <- ribge::populacao_municipios(2024)
# write_tsv(pop, file = "input/pop2024.csv")


def baixar_arquivo_ftp(diretorio: str, nome_arquivo: str, destino: Path,
                       host: str = FTP_HOST) -> None:
    ftp = FTP(host)
    ftp.set_pasv(False)   #  importante para o DATASUS
    ftp.login()           #  login anônimo sem argumentos
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

if fil:
  ja_baixados = set(fil)
faltando = [f for f in filenames if f not in ja_baixados]

print("-" * 74)
print(f"Aviso: Existem {len(filenames)} arquivos no sitio pesquisado")
print(f"Aviso: Existem {len(faltando)} arquivos para atualizar")
print("-" * 74)

for nome in faltando:
  baixar_arquivo_ftp(FTP_DIR, nome, MYPATH / nome)
else:
  print("-" * 74)
print(f"Aviso: Existem {len(filenames)} arquivos no sitio pesquisado")
print(f"Aviso: Existem {len(filenames)} arquivos para atualizar")
print("-" * 74)

for nome in filenames:
  baixar_arquivo_ftp(FTP_DIR, nome, MYPATH / nome)

# ========== 3. CONVERSÃO .dbc -> .tsv ==========
files_dbc = [f for f in os.listdir(MYPATH) if f.endswith(".dbc")]
files_tsv_existentes = [f.replace(".tsv", "") for f in os.listdir(DIR_TSV)]

pendentes = sorted(
  set(f.replace(".dbc", "") for f in files_dbc) - set(files_tsv_existentes)
)

print("Arquivos pendentes de conversão:", len(pendentes))
print(pendentes)

for file_base in pendentes:
  dbc_path = MYPATH / f"{file_base}.dbc"
  tsv_path = DIR_TSV / f"{file_base}.tsv"

try:

  base = pyreaddbc.readdbc(str(dbc_path), encoding="latin1")
  base.to_csv(tsv_path, sep="\t", index=False)
  print(file_base, "ok -")
except Exception as e:
  print("ERRO em", file_base, ":", e)

# ========== 4. CONSOLIDAÇÃO POR SEMANA EPIDEMIOLÓGICA (BAHIA / SINAN) ==========
myfiles = sorted(f for f in os.listdir(DIR_TSV) if f.startswith(SUF))
anos = [int(re.search(r"\d+", f).group()) for f in myfiles]
myfiles = [f for f, a in zip(myfiles, anos) if a >= 13]

calendario = pd.read_csv(DIR / "sinan_calendario.txt", sep="\t")
# ajuste o separador acima se o arquivo original usar vírgula em vez de tab

confirmados = True
lista_bahia = []

leve     = {1, 6, 10}
moderada = {2, 7, 11}
grave    = {3, 4, 8, 12}

RACE_MAP = {1: "Branca", 2: "Preta", 3: "Amarela", 4: "Parda", 5: "Indigena", 9: "Ignorado"}


def calc_idade_padrao(age_temp) -> float:
  s = str(age_temp)
  if len(s) == 2:
    return float(s)
  if s[:2] == "40":
    return float(s[2:4])
  return 0.0


def calc_idade_alt(age_temp) -> float:
  s = str(age_temp)
  if s[:1] in ("M", "D", "I"):
    return 0.0
  if s[:1] == "A":
    return float(s[1:4])
  if len(s) == 2:
    return float(s)
  return float(s[2:4])


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

temp_agre.columns = ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
                     "Age_temp", "Sex", "Race_Colour", "New_Cases"]

temp_agre["Noti_Date"] = pd.to_datetime(temp_agre["Noti_Date"])
temp_agre["Race_Colour"] = temp_agre["Race_Colour"].map(RACE_MAP)
temp_agre["Age"] = temp_agre["Age_temp"].apply(calc_idade_padrao)

temp_agre_final = temp_agre[
  ["Noti_Date", "Noti_Week", "weekStart", "State", "City",
   "New_Cases", "Age", "Sex", "Race_Colour"]
].copy()

temp_agre_final["City"] = pd.to_numeric(temp_agre_final["City"], errors="coerce")
temp_agre_final["Noti_Week"] = temp_agre_final["Noti_Week"].astype("Int64")

lista_bahia.append(temp_agre_final)
del temp_file, temp, temp_agre, temp_agre_final
gc.collect()

newBahia = pd.concat(lista_bahia, ignore_index=True)
newBahia["State"] = pd.to_numeric(newBahia["State"])

# ========== POPULAÇÃO (equivalente a ribge::populacao_municipios(2024)) ==========
# Não existe pacote Python equivalente ao `ribge`. solucao:
#  rodar no R `write.csv(pop2024, "pop2024.csv", row.names = FALSE)` uma
#      vez e carregar esse CSV aqui.
# Abaixo assume-se a opção (1).
pop2024 = pd.read_csv(
  DIR / "pop2024.csv",
  dtype={"cod_municipio": str, "cod_munic6": str},
)

meso_regiao = pd.read_excel(
  DIR / "regioes_geograficas_composicao_por_municipios_2017_20180911.xls"
)

meso_regiao_pop = pop2024.merge(
  meso_regiao, left_on="cod_municipio", right_on="CD_GEOCODI", how="left"
)

baseFinal = newBahia.merge(
  meso_regiao_pop,
  left_on=["State", "City"],
  right_on=["codigo_uf", "cod_munic6"],
  how="left",
)

# estados.rds (objeto sf) -> pyreadr devolve um dict {nome_objeto: DataFrame}
estados_result = pyreadr.read_r(str(DIR / "estados.rds"))
estado = next(iter(estados_result.values()))
if "geometry" in estado.columns:
  estado = estado.drop(columns=["geometry"])

baseFinal = baseFinal.merge(
  estado[["code_state", "abbrev_state", "name_state", "name_region"]],
  left_on="State", right_on="code_state", how="left",
)

out_name = (
  "2014-2025_DENGUE_CONFIRMADOS_dash_new.tsv"
  if confirmados else
    "2014-2025_DENGUE_NOTIFICADOS_dash_new.tsv"
)
baseFinal.to_csv(DIR / out_name, sep="\t", index=False)

del newBahia, baseFinal, meso_regiao, meso_regiao_pop
gc.collect()

# ========== "PARA ZE": granularidade diária, sem semana epidemiológica ==========
arquivos_tsv = sorted(f for f in os.listdir(DIR_TSV) if f.startswith(SUF))
anos = [int(re.search(r"\d+", f).group()) for f in arquivos_tsv]
t = [f for f, a in zip(arquivos_tsv, anos) if a >= 13]

confirmados = False
lista_newData = []

COLS_ZE = {
  "DT_NOTIFIC", "SEM_NOT", "SG_UF_NOT", "ID_MUNICIP",
  "NU_IDADE_N", "CS_SEXO", "CS_RACA", "CLASSI_FIN", "CRITERIO",
  "CON_CLASSI", "CON_CRITER", "NU_IDADE", "total",
}

for f in t:
  print(f)
base = pd.read_csv(
  DIR_TSV / f, sep="\t", low_memory=False,
  usecols=lambda c: c in COLS_ZE,
)

rename_map = {}
if "CON_CLASSI" in base.columns:
  rename_map["CON_CLASSI"] = "CLASSI_FIN"
if "CON_CRITER" in base.columns:
  rename_map["CON_CRITER"] = "CRITERIO"
idade_alt = "NU_IDADE" in base.columns
if idade_alt:
  rename_map["NU_IDADE"] = "NU_IDADE_N"
base = base.rename(columns=rename_map)

base["Dengue_class"] = pd.NA
base.loc[base["CLASSI_FIN"].isin(leve), "Dengue_class"] = "1"
base.loc[base["CLASSI_FIN"].isin(moderada), "Dengue_class"] = "2"
base.loc[base["CLASSI_FIN"].isin(grave), "Dengue_class"] = "3"

if confirmados:
  base_temp = base[(base["CRITERIO"] < 3) & base["Dengue_class"].notna()].copy()
else:
  base_temp = base.copy()

base_temp["Noti_Year"] = int("20" + re.sub(r"[^0-9]", "", f))

group_cols = ["DT_NOTIFIC", "SEM_NOT", "Noti_Year", "SG_UF_NOT",
              "ID_MUNICIP", "NU_IDADE_N", "CS_SEXO", "CS_RACA"]

if "total" in base_temp.columns:
  temp_agre = (
    base_temp.groupby(group_cols, as_index=False)["total"]
    .sum()
    .rename(columns={"total": "new_cases"})
    .dropna()
  )
else:
  temp_agre = (
    base_temp.groupby(group_cols, as_index=False)
    .size()
    .rename(columns={"size": "new_cases"})
    .dropna()
  )

temp_agre.columns = ["Noti_Date", "Noti_Week", "Noti_Year", "State", "City",
                     "Age_temp", "Sex", "Race_Colour", "New_Cases"]
temp_agre["Noti_Date"] = pd.to_datetime(temp_agre["Noti_Date"])
temp_agre["Race_Colour"] = temp_agre["Race_Colour"].map(RACE_MAP)
temp_agre["Age"] = temp_agre["Age_temp"].apply(
  calc_idade_alt if idade_alt else calc_idade_padrao
)

temp_agre_final = temp_agre[
  ["Noti_Date", "Noti_Week", "Noti_Year", "State", "City",
   "New_Cases", "Age", "Sex", "Race_Colour"]
].copy()
temp_agre_final["City"] = pd.to_numeric(temp_agre_final["City"], errors="coerce")

lista_newData.append(temp_agre_final)
del base, base_temp, temp_agre, temp_agre_final
gc.collect()

newData = pd.concat(lista_newData, ignore_index=True)

# --- joins finais: cada um resolve um par de colunas de tipos diferentes ---
# 1) City (6 dígitos) <-> cod_munic6 (não cod_municipio, que tem 7 dígitos)
newData["City"] = newData["City"].astype("Int64").astype(str)
pop2024["cod_munic6"] = pop2024["cod_munic6"].astype(str)
newData = newData.merge(pop2024, left_on="City", right_on="cod_munic6", how="left")

# 2) State (numérico) <-> code_state
newData["State"] = pd.to_numeric(newData["State"])
newData = newData.merge(
  estado[["code_state", "abbrev_state", "name_state", "name_region"]],
  left_on="State", right_on="code_state", how="left",
)

out_name = (
  "2000-2025_DENGUE_CONFIRMADOS_new_ze.tsv"
  if confirmados else
    "2000-2025_DENGUE_NOTIFICADOS_new_ze.tsv"
)
newData.to_csv(DIR / out_name, sep="\t", index=False)

# pop    <- ribge::populacao_municipios(2024)
# write()
# write_tsv(pop, file = "input/pop2024.csv")
