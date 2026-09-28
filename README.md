# 📊 PricePulse — Dynamic Pricing & Revenue Intelligence

PricePulse is an end-to-end business analytics project that analyzes sales, demand, pricing, competitor pricing, discounts, promotions, inventory, and seasonal patterns to generate actionable business insights.

The project combines **Python, Pandas, MySQL, SQL, and Power BI** to transform raw sales data into an interactive pricing and revenue intelligence solution.

---

## 🎯 Business Problem

Businesses need to make pricing decisions while considering multiple factors such as:

- Customer demand
- Product pricing
- Competitor pricing
- Inventory availability
- Discounts
- Promotions
- Seasonality
- Regional performance

PricePulse analyzes these factors together to help identify pricing patterns, demand behavior, revenue opportunities, and inventory risks.

---

## 🚀 Project Objectives

The main objectives of PricePulse are to:

- Analyze historical sales and demand patterns
- Understand the relationship between price and demand
- Compare product pricing with competitor pricing
- Analyze the impact of discounts and promotions
- Identify high-demand and low-inventory products
- Analyze revenue across product categories
- Understand seasonal demand patterns
- Build an interactive Power BI dashboard
- Convert raw data into business-oriented insights

---

# 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database | MySQL |
| Querying | SQL |
| Visualization | Power BI, Matplotlib |
| Development | VS Code |
| Version Control | Git, GitHub |

---

# 📂 Project Structure

```text
PRICE PULSE/
│
├── DATA/
│   ├── RAW/
│   │   └── sales_data.csv
│   │
│   └── PROCESSED/
│       └── sales_data_features.csv
│
├── PYTHON/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── load_mysql.py
│
├── SQL/
│   └── pricing_analysis.sql
│
├── POWER BI/
│   └── PricePulse_Dynamic_Pricing.pbix
│
├── SCREENSHOTS/
│   └── dashboard.png
│
├── DOCUMENTATIONS/
│
├── MODELS/
│
├── README.md
└── .gitignore

# PricePulse — Project Documentation

## 1. Project Overview

PricePulse is a Dynamic Pricing and Revenue Intelligence project developed to analyze sales, demand, pricing, competitor pricing, discounts, promotions, inventory, and seasonal patterns.

The project follows an end-to-end business analytics workflow using:

- Python
- Pandas
- NumPy
- MySQL
- SQL
- Power BI
- Git & GitHub

The objective is to convert raw sales data into structured business insights that can support pricing, revenue, promotion, and inventory analysis.

---

# 2. Business Problem

Businesses need to understand how different factors affect product sales and demand.

Important factors include:

- Product price
- Competitor price
- Customer demand
- Units sold
- Inventory
- Discounts
- Promotions
- Seasonality
- Region

PricePulse analyzes these variables together to provide a structured view of pricing and demand behavior.

---

# 3. Project Objectives

The main objectives of the project are:

1. Inspect and understand the raw sales dataset.
2. Clean and prepare the data for analysis.
3. Create business-oriented features using Python.
4. Store the processed data in MySQL.
5. Perform business analysis using SQL.
6. Build an interactive Power BI dashboard.
7. Analyze pricing, demand, revenue, promotions, discounts, and inventory.
8. Present the results in a recruiter-friendly business analytics project.

---

# 4. Dataset

The dataset contains 76,000 records and 16 original variables.

### Original Variables

| Variable | Description |
|---|---|
| Date | Date of the sales record |
| Store ID | Unique identifier for the store |
| Product ID | Unique identifier for the product |
| Category | Product category |
| Region | Geographic region |
| Inventory Level | Available inventory |
| Units Sold | Number of units sold |
| Units Ordered | Number of units ordered |
| Price | Product selling price |
| Discount | Discount percentage |
| Weather Condition | Weather condition |
| Promotion | Promotion indicator |
| Competitor Pricing | Competitor product price |
| Seasonality | Seasonal classification |
| Epidemic | Epidemic-related indicator |
| Demand | Product demand |

---

# 5. Data Inspection

Python and Pandas were used to inspect the raw dataset before performing transformations.

### Inspection Activities

- Checked dataset dimensions
- Checked column names
- Checked data types
- Checked missing values
- Checked duplicate records
- Checked unique values
- Generated descriptive statistics
- Reviewed numerical variables

### Initial Results

- Records: 76,000
- Original columns: 16
- Missing values: 0
- Duplicate rows: 0

The inspection confirmed that the dataset was suitable for further processing.

---

# 6. Data Cleaning

The raw dataset was prepared for analysis using Python.

### Cleaning Steps

1. Validated column data types.
2. Converted the Date column into the appropriate date format.
3. Checked for missing values.
4. Checked for duplicate records.
5. Validated numerical columns.
6. Standardized data where required.
7. Prepared the dataset for feature engineering.

The cleaned data was then passed to the feature engineering stage.

---

# 7. Feature Engineering

Feature engineering was performed to convert the raw dataset into a more business-oriented analytical dataset.

## 7.1 Revenue

Revenue was calculated using:

Revenue = Price × Units Sold

This metric measures the sales value generated from each product record.

---

## 7.2 Net Price

Net Price represents the effective price after applying the discount.

Net Price = Price × (1 - Discount / 100)

This allows pricing analysis to consider the effect of discounts.

---

## 7.3 Competitor Price Difference

The difference between the company's product price and competitor pricing was calculated as:

Price Difference = Price - Competitor Pricing

This helps identify whether a product is priced above or below its competitor.

---

## 7.4 Inventory Gap

Inventory Gap was calculated as:

Inventory Gap = Inventory Level - Demand

This helps understand the relationship between available inventory and expected demand.

---

## 7.5 Inventory Coverage Ratio

Inventory Coverage Ratio was created to compare available inventory with demand.

This provides an additional indicator for understanding inventory availability.

---

## 7.6 Price Position

Products were categorized based on their price relative to competitors.

Possible categories include:

- Above Competitor
- Below Competitor
- Competitive

---

## 7.7 Demand Level

Demand was grouped into business-friendly categories:

- Low
- Medium
- High

These categories make the data easier to analyze in SQL and Power BI.

---

# 8. Processed Dataset

After feature engineering, the processed dataset contained the original variables together with additional analytical features.

The processed data was used for:

- SQL analysis
- Power BI visualization
- Business interpretation

---

# 9. MySQL Database

The processed dataset was loaded into MySQL.

### Database Name

pricepulse

### Main Table

sales_data

The MySQL database provides a structured environment for performing business queries.

---

# 10. SQL Analysis

SQL was used to answer business questions from the processed dataset.

## 10.1 Revenue Analysis

Queries were created to analyze:

- Total revenue
- Revenue by category
- Product-level revenue
- Revenue patterns

---

## 10.2 Demand Analysis

Demand analysis included:

- Total demand
- Demand by category
- Demand across seasons
- Product demand patterns

---

## 10.3 Pricing Analysis

Pricing analysis included:

- Product price
- Competitor price
- Price difference
- Price position
- Relationship between pricing and demand

---

## 10.4 Promotion Analysis

Promotion-related analysis compared:

- Promotional periods
- Non-promotional periods
- Demand performance

---

## 10.5 Discount Analysis

Discount analysis examined the relationship between:

- Discount percentage
- Units sold
- Demand
- Revenue

---

## 10.6 Inventory Analysis

Inventory analysis examined:

- Inventory level
- Demand
- Inventory gap
- Inventory coverage

This helps identify products where inventory availability may require attention.

---

# 11. Power BI Dashboard

The processed dataset was imported into Power BI to create an interactive Dynamic Pricing & Revenue Intelligence Dashboard.

The dashboard converts the SQL and Python analysis into visual business insights.

---

# 12. Dashboard KPIs

The dashboard contains the following key performance indicators:

- Total Revenue
- Units Sold
- Total Demand
- Average Price
- Average Demand

These KPIs provide a high-level summary of the dataset.

---

# 13. Dashboard Visualizations

## Revenue by Product Category

Shows how revenue is distributed across product categories.

## Demand by Product Category

Compares demand across different product categories.

## Price vs Competitor Pricing

Compares product pricing against competitor pricing.

## Promotion Impact on Demand

Shows differences in demand between promotional and non-promotional periods.

## Discount Impact on Units Sold

Analyzes the relationship between discount levels and units sold.

## Inventory Level vs Demand

Compares available inventory with demand to highlight inventory patterns.

---

# 14. Dashboard Filters

Interactive Power BI slicers were added for:

- Region
- Category
- Seasonality
- Promotion

These filters allow users to analyze the dashboard from different business perspectives.

---

# 15. Business Questions

PricePulse was designed to answer questions such as:

### Revenue

- Which categories generate the most revenue?
- Which products contribute significantly to revenue?

### Demand

- Which categories have higher demand?
- How does demand change across seasons?

### Pricing

- How does product pricing compare with competitors?
- Which products are above or below competitor pricing?
- How does pricing relate to demand?

### Promotions and Discounts

- How does demand change during promotions?
- How do discounts relate to units sold?

### Inventory

- Which products have high demand relative to inventory?
- Where could inventory availability become a concern?

---

# 16. Technology Stack

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Database

- MySQL

## Query Language

- SQL

## Business Intelligence

- Power BI

## Development Tools

- VS Code
- Git
- GitHub

---

# 17. Project Architecture

The complete project follows this pipeline:

Raw Data

↓

Python Data Inspection

↓

Data Cleaning

↓

Feature Engineering

↓

Processed Dataset

↓

MySQL Database

↓

SQL Business Analysis

↓

Power BI Dashboard

↓

Business Insights

---

# 18. Project Files

The project is organized into the following components:

```text
PRICE PULSE/
│
├── DATA/
│   ├── RAW/
│   └── PROCESSED/
│
├── PYTHON/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── load_mysql.py
│
├── SQL/
│   └── pricing_analysis.sql
│
├── POWER BI/
│   └── PricePulse_Dynamic_Pricing.pbix
│
├── SCREENSHOTS/
│   └── dashboard.png
│
├── DOCUMENTATIONS/
│   └── PricePulse_Project_Documentation.md
│
├── MODELS/
│
├── README.md
└── .gitignore


B.Tech — Electrical & Computer Engineering
Thapar Institute of Engineering and Technology

Connect
LinkedIn: Sneha Chatrath
