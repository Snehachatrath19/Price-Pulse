import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "DATA" / "PROCESSED" / "sales_data_clean.csv"
OUTPUT_FILE = BASE_DIR / "DATA" / "PROCESSED" / "sales_data_features.csv"


# --------------------------------------------------
# 2. LOAD CLEAN DATA
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("===== DATA LOADED =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------------------------
# 3. CONVERT DATE
# --------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])


# --------------------------------------------------
# 4. REVENUE
# --------------------------------------------------

df["Revenue"] = df["Price"] * df["Units Sold"]


# --------------------------------------------------
# 5. DISCOUNT AMOUNT
# --------------------------------------------------

df["Discount Amount"] = (
    df["Price"] * df["Discount"] / 100
)


# --------------------------------------------------
# 6. NET PRICE
# --------------------------------------------------

df["Net Price"] = df["Price"] - df["Discount Amount"]


# --------------------------------------------------
# 7. COMPETITOR PRICE DIFFERENCE
# --------------------------------------------------

df["Competitor Price Difference"] = (
    df["Price"] - df["Competitor Pricing"]
)


# --------------------------------------------------
# 8. COMPETITOR PRICE GAP %
# --------------------------------------------------

df["Competitor Price Gap %"] = (
    df["Competitor Price Difference"]
    / df["Competitor Pricing"]
) * 100


# --------------------------------------------------
# 9. INVENTORY GAP
# --------------------------------------------------

df["Inventory Gap"] = (
    df["Inventory Level"] - df["Units Sold"]
)


# --------------------------------------------------
# 10. INVENTORY COVERAGE
# --------------------------------------------------

df["Inventory Coverage Ratio"] = (
    df["Inventory Level"]
    / df["Units Sold"].replace(0, pd.NA)
)


# --------------------------------------------------
# 11. PRICE POSITION
# --------------------------------------------------

df["Price Position"] = df.apply(
    lambda row:
        "Above Competitor"
        if row["Price"] > row["Competitor Pricing"]
        else "Below Competitor"
        if row["Price"] < row["Competitor Pricing"]
        else "Same as Competitor",
    axis=1
)


# --------------------------------------------------
# 12. DEMAND LEVEL
# --------------------------------------------------

df["Demand Level"] = pd.cut(
    df["Demand"],
    bins=[0, 75, 150, float("inf")],
    labels=["Low", "Medium", "High"]
)


# --------------------------------------------------
# 13. DISPLAY RESULTS
# --------------------------------------------------

print("\n===== NEW FEATURES =====")

new_columns = [
    "Revenue",
    "Discount Amount",
    "Net Price",
    "Competitor Price Difference",
    "Competitor Price Gap %",
    "Inventory Gap",
    "Inventory Coverage Ratio",
    "Price Position",
    "Demand Level"
]

print(df[new_columns].head())


# --------------------------------------------------
# 14. SUMMARY
# --------------------------------------------------

print("\n===== BUSINESS SUMMARY =====")

print("Total Revenue:", round(df["Revenue"].sum(), 2))

print(
    "Average Net Price:",
    round(df["Net Price"].mean(), 2)
)

print(
    "Average Discount:",
    round(df["Discount"].mean(), 2), "%"
)

print(
    "Average Demand:",
    round(df["Demand"].mean(), 2)
)


# --------------------------------------------------
# 15. SAVE FEATURE DATASET
# --------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\n===== FEATURE ENGINEERING COMPLETE =====")
print("New columns:", len(new_columns))
print("Final columns:", df.shape[1])
print("Saved to:")
print(OUTPUT_FILE)