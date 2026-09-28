import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parents[1]

# Dataset location
DATA_PATH = BASE_DIR / "data" / "raw" / "sales_data.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== BASIC STATISTICS =====")
print(df.describe(include="all"))