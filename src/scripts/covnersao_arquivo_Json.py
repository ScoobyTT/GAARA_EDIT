import json
from pathlib import Path
import pandas as pd

# rode da raiz do projeto (GAARA_EDIT), senão os caminhos relativos não batem
RAW_not = Path("src/data/2014-2025_DENGUE_NOTIFICADOS_dash_new.tsv")
RAW_conf = Path("src/data/2014-2025_DENGUE_CONFIRMADOS_dash_new.tsv")  # ainda não usado
OUT = Path("src/data/vacinacao")
OUT.mkdir(parents=True, exist_ok=True)

SEP = "\t"  # troque para ";" se o arquivo for separado por ponto e vírgula

df = pd.read_csv(RAW_not, sep=SEP, dtype="object")

# 1) tipos e id
df["New_Cases"] = pd.to_numeric(df["New_Cases"], errors="coerce").fillna(0).astype(int)
df["id"] = range(1, len(df) + 1)

# 2) registros completos (colunas que não existirem no arquivo são avisadas e ignoradas)
COLS = [
    "id", "Noti_Date", "Noti_Week", "weekStart", "State", "City", "New_Cases",
    "Age", "Sex", "Race_Colour", "EVOLUCAO", "uf", "codigo_uf", "codigo_munic",
    "nome_munic", "populacao_str", "populacao", "cod_munic6", "cod_municipio",
    "nome_mun", "CD_GEOCODI", "cod_rgi", "nome_rgi", "cod_rgint", "nome_rgint",
    "code_state", "abbrev_state", "name_state", "name_region",
]
missing = [c for c in COLS if c not in df.columns]
if missing:
    print("Colunas ausentes no arquivo:", missing)
cols = [c for c in COLS if c in df.columns]

registros = df[cols].astype(object).where(df[cols].notna(), None)  # NaN -> null
with open(OUT / "vacinados_percent_uf.json", "w", encoding="utf-8") as f:
    json.dump(registros.to_dict(orient="records"), f, ensure_ascii=False)

# 3) série semanal por estado, no formato {coluna: {"0": valor, "1": valor, ...}}
semana = (
    df.groupby(["Noti_Week", "name_state"], as_index=False)["New_Cases"]
      .sum()
)
with open(OUT / "week_vacina_1dose.json", "w", encoding="utf-8") as f:
    json.dump(semana.to_dict(), f, ensure_ascii=False, indent=2) 


print("arquivos convertidos com sucesso!")
