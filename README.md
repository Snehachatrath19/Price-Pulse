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
1. Data Inspection

The first stage involved inspecting the raw sales dataset using Python and Pandas.

The dataset contains 76,000 records and includes 16 original variables:

Date
Store ID
Product ID
Category
Region
Inventory Level
Units Sold
Units Ordered
Price
Discount
Weather Condition
Promotion
Competitor Pricing
Seasonality
Epidemic
Demand
Data Quality Checks

The inspection process checked:

Dataset dimensions
Data types
Missing values
Duplicate records
Unique values
Basic statistical information

The initial inspection showed:

76,000 records
16 original columns
No missing values
No duplicate rows
🧹 2. Data Cleaning

The raw dataset was cleaned and prepared for analysis using Python.

Cleaning Steps
Validated data types
Converted date fields
Checked missing values
Checked duplicate records
Standardized numerical variables
Prepared the dataset for feature engineering

The cleaned dataset was then used for the next stage of the pipeline.

⚙️ 3. Feature Engineering

Business-oriented features were created to make the dataset more useful for pricing and revenue analysis.

Revenue

Revenue was calculated using:

Revenue = Price × Units Sold
Net Price

The effective selling price after applying the discount.

Net Price = Price × (1 - Discount / 100)
Competitor Price Difference

Used to compare the company's product price against competitor pricing.

Price Difference = Price - Competitor Pricing
Inventory Gap

Used to understand the relationship between inventory availability and demand.

Inventory Gap = Inventory Level - Demand
Inventory Coverage Ratio

Used to understand how much demand can potentially be covered by available inventory.

Price Position

Products were categorized based on their pricing relative to competitors, such as:

Above Competitor
Below Competitor
Competitive
Demand Level

Demand was categorized into meaningful business segments such as:

Low
Medium
High

These engineered features were later used in SQL analysis and the Power BI dashboard.

🗄️ 4. MySQL Database

The processed dataset was loaded into MySQL for structured business analysis.

Database
pricepulse
Main Table
sales_data

The database contains the processed sales records along with the engineered pricing and business features.

SQL was then used to perform structured analysis on the dataset.

📈 5. SQL Business Analysis

The SQL analysis focuses on pricing, demand, revenue, promotion, discount, and inventory-related business questions.

Revenue Analysis

Analyzed:

Total revenue
Revenue by category
Revenue performance across products
Demand Analysis

Analyzed:

Total demand
Demand by category
Demand patterns across seasons
Pricing Analysis

Compared:

Product price
Competitor price
Price position
Pricing and demand patterns
Promotion Analysis

Compared demand performance during:

Promotional periods
Non-promotional periods
Discount Analysis

Analyzed how different discount levels relate to:

Units sold
Demand
Revenue
Inventory Analysis

Analyzed inventory availability relative to demand to identify potential inventory risk.

📊 6. Power BI Dashboard

The processed dataset was imported into Power BI to create an interactive Dynamic Pricing & Revenue Intelligence Dashboard.

Key Performance Indicators

The dashboard includes:

Total Revenue
Units Sold
Total Demand
Average Price
Average Demand
Main Visualizations
Revenue by Product Category

Shows revenue contribution across different product categories.

Demand by Product Category

Compares demand levels across categories.

Price vs Competitor Pricing

Compares average product pricing against competitor pricing over time.

Promotion Impact on Demand

Compares demand during promotional and non-promotional periods.

Discount Impact on Units Sold

Analyzes the relationship between discount levels and units sold.

Inventory Level vs Demand

Helps identify products where demand is high relative to available inventory.

🎛️ Interactive Dashboard Filters

The dashboard includes interactive slicers for:

Region
Category
Seasonality
Promotion

These filters allow users to explore the analysis from different business perspectives.

💡 Business Questions Answered

PricePulse helps answer questions such as:

Revenue
Which product categories generate the most revenue?
Which products contribute significantly to revenue?
Demand
Which categories have the highest demand?
How does demand vary across different seasons?
Pricing
How does our pricing compare with competitors?
Which products are priced above or below competitors?
How does pricing relate to demand?
Promotions & Discounts
Does demand change during promotional periods?
How do different discount levels relate to units sold?
Inventory
Which products have high demand relative to inventory?
Where could inventory availability become a business concern?
📌 Key Skills Demonstrated
Data Analytics
Data Cleaning
Exploratory Data Analysis
Feature Engineering
Business Analysis
Data Interpretation
Python
Python
Pandas
NumPy
SQL & Database
SQL
MySQL
Aggregations
GROUP BY
Filtering
Business Query Analysis
Business Intelligence
Power BI
Interactive Dashboards
KPI Development
Data Visualization
Slicers
Business Storytelling
Development
VS Code
Git
GitHub
📸 Dashboard Preview

📊 Key Project Metrics
Metric	Value
Records Analyzed	76,000
Original Variables	16
Database	MySQL
Main Table	sales_data
Dashboard	Power BI
Analysis	SQL + Python
Pricing Features	Engineered
🔮 Future Improvements

The current version focuses on analytics and business intelligence.

Future versions could extend PricePulse with:

Demand forecasting
Price elasticity analysis
Machine learning-based demand prediction
Automated pricing recommendations
Competitor price monitoring
Revenue optimization
What-if pricing scenarios
Dynamic pricing recommendations
👩‍💻 Author
Sneha Chatrath

B.Tech — Electrical & Computer Engineering
Thapar Institute of Engineering and Technology

Connect
LinkedIn: Sneha Chatrath
