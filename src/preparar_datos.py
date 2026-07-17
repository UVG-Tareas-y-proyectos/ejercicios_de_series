"""Limpieza y separacion train/test. Genera data/processed/train.csv y test.csv"""
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE / "data/raw/guatemala_temperatura.csv", parse_dates=["month"])

# sin duplicados ni nulos
df = df.sort_values("month").drop_duplicates(subset="month").dropna().reset_index(drop=True)

# ultimos 36 meses para prueba
train = df.iloc[:-36]
test = df.iloc[-36:]

(BASE / "data/processed").mkdir(parents=True, exist_ok=True)
train.to_csv(BASE / "data/processed/train.csv", index=False)
test.to_csv(BASE / "data/processed/test.csv", index=False)
print("train:", train.shape, " test:", test.shape)
