import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA = BASE_DIR / "DATA" / "RAW" / "sales_data.csv"
PROCESSED_DATA = BASE_DIR / "DATA" / "PROCESSED" / "sales_data_clean.csv"


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(RAW_DATA)

print("===== ORIGINAL DATA =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------------------------
# 3. STANDARDIZE COLUMN NAMES
# --------------------------------------------------

df.columns = df.columns.str.strip()

print("\n===== COLUMNS =====")
print(df.columns.tolist())


# --------------------------------------------------
# 4. CONVERT DATE
# --------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


# --------------------------------------------------
# 5. REMOVE DUPLICATES
# --------------------------------------------------

duplicates = df.duplicated().sum()

print("\n===== DUPLICATES =====")
print("Duplicate rows:", duplicates)

df = df.drop_duplicates()


# --------------------------------------------------
# 6. CHECK MISSING VALUES
# --------------------------------------------------

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# --------------------------------------------------
# 7. STANDARDIZE TEXT COLUMNS
# --------------------------------------------------

text_columns = [
    "Store ID",
    "Product ID",
    "Category",
    "Region",
    "Weather Condition",
    "Seasonality"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# --------------------------------------------------
# 8. NUMERIC COLUMNS
# --------------------------------------------------

numeric_columns = [
    "Inventory Level",
    "Units Sold",
    "Units Ordered",
    "Price",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Epidemic",
    "Demand"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# --------------------------------------------------
# 9. DATA VALIDATION
# --------------------------------------------------

print("\n===== DATA VALIDATION =====")

print("\nNegative Inventory:")
print((df["Inventory Level"] < 0).sum())

print("\nNegative Units Sold:")
print((df["Units Sold"] < 0).sum())

print("\nNegative Units Ordered:")
print((df["Units Ordered"] < 0).sum())

print("\nNegative Price:")
print((df["Price"] < 0).sum())

print("\nNegative Competitor Pricing:")
print((df["Competitor Pricing"] < 0).sum())

print("\nNegative Demand:")
print((df["Demand"] < 0).sum())


# --------------------------------------------------
# 10. FINAL INFORMATION
# --------------------------------------------------

print("\n===== CLEAN DATA =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== DATA TYPES =====")
print(df.dtypes)


# --------------------------------------------------
# 11. SAVE CLEAN DATA
# --------------------------------------------------

PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_DATA, index=False)

print("\n===== CLEANING COMPLETE =====")
print("Saved cleaned dataset to:")
print(PROCESSED_DATA)