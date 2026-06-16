# 📊 Vendor Sales Performance Analysis

A comprehensive Vendor Sales Performance Analysis project designed to evaluate vendor contribution, product profitability, inventory efficiency, and procurement effectiveness using sales, purchase, pricing, and invoice data.

Built using **Python, SQL, MySQL, Pandas, and Data Visualization libraries**, this project transforms raw business transaction data into meaningful KPIs and actionable insights that support vendor management, inventory optimization, and strategic business decisions.

---

## 🚀 Features

### 🏢 Vendor Performance Analysis

Analyze vendor contribution, purchase volume, and revenue generation across multiple suppliers.

### 💰 Profitability Analysis

Calculate Gross Profit and Profit Margin to evaluate business performance and vendor profitability.

### 📦 Inventory Analysis

Measure inventory efficiency using Stock Turnover Ratio and sales movement metrics.

### 📈 Sales Performance Analysis

Analyze total sales, purchase costs, and revenue trends across vendors and products.

### 🛒 Product Profitability Analysis

Identify high-margin products and compare sales performance across product categories.

### 📊 Vendor Contribution Analysis

Determine which vendors contribute the highest percentage of total purchases and sales.

### 🔗 Database Integration

Extract and combine data from multiple MySQL tables using SQL queries and Python.

### 📉 Correlation Analysis

Identify relationships between sales, purchases, inventory, and profitability metrics.

---

## 🗄️ Database Overview

The project integrates data from multiple relational database tables:

### Tables Used

* `purchases`
* `sales`
* `vendor_invoice`
* `purchase_prices`

```text
purchases         → Product purchase transactions
sales             → Product sales transactions
vendor_invoice    → Vendor invoice details
purchase_prices   → Product pricing information
```

---

## 🧹 Data Preparation

### Data Cleaning Tasks

* Extracted data from MySQL database.
* Performed SQL joins and aggregations.
* Handled missing values using appropriate techniques.
* Standardized vendor names and text fields.
* Converted numerical columns into suitable data types.
* Removed inconsistencies and duplicate records.
* Created business KPIs through feature engineering.

Example:

```python
df.fillna(0)
df['VendorName'] = df['VendorName'].str.strip()
df['Volume'] = df['Volume'].astype('float64')
```

---

## 📊 Key Performance Indicators (KPIs)

### 💵 Gross Profit

Measures actual profit earned after purchase costs.

```python
GrossProfit = TotalSalesDollars - totalPPrice
```

---

### 📈 Profit Margin

Measures profitability percentage.

```python
ProfitMargin = (GrossProfit / TotalSalesDollars) * 100
```

---

### 📦 Stock Turnover Ratio

Measures inventory movement efficiency.

```python
StockTurnover = TotalSalesQuantity / totalQuantity
```

---

### 💹 Sales-to-Purchase Ratio

Measures revenue generated against purchase cost.

```python
SalesToPurchaseRatio = TotalSalesDollars / totalPPrice
```

---

## 🔍 Exploratory Data Analysis

### Vendor Analysis

* Top Vendors by Sales Revenue
* Vendor Purchase Contribution
* Vendor Profitability Comparison

### Product Analysis

* High Margin Products
* Low Margin Products
* Product Sales Performance

### Inventory Analysis

* Stock Turnover Evaluation
* Inventory Movement Trends

### Profitability Analysis

* Gross Profit Distribution
* Profit Margin Analysis
* Vendor-wise Profit Contribution

### Business Performance Analysis

* Revenue Trends
* Sales-to-Purchase Ratio Analysis
* Correlation Between Business Metrics

---

## 📈 Visualizations Used

* Bar Charts
* Histograms
* Pie Charts
* Box Plots
* Correlation Heatmaps
* Distribution Plots
* Vendor Contribution Charts

Example:

```python
sns.heatmap(correlation_matrix, annot=True)
```

---

## 🛠️ Tech Stack

* Python
* SQL
* MySQL
* Pandas
* SQLAlchemy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 📁 Project Structure

```text
vendor-sales-analysis/
│
├── sql/
│   ├── vendor_queries.sql
│   └── data_extraction.sql
│
├── notebooks/
│   └── vendor_sales_analysis.ipynb
│
├── data/
│   └── vendor_sales_dataset.csv
│
├── visualizations/
│   ├── vendor_contribution.png
│   ├── profit_margin_analysis.png
│   ├── stock_turnover.png
│   └── correlation_heatmap.png
│
├── requirements.txt
└── README.md
```

---

## 🎯 Key Findings

* A small number of vendors contributed a significant percentage of total sales revenue.
* Several products generated high profit margins despite moderate sales volumes.
* Vendor profitability varied across different product categories.
* Inventory turnover highlighted products with faster stock movement.
* Sales-to-Purchase Ratio revealed operational efficiency across vendors.
* Vendor contribution analysis helped identify critical business partners.

---

## 📌 Business Impact

This project helps organizations:

* Improve vendor selection strategies.
* Optimize procurement and purchasing decisions.
* Identify highly profitable vendors and products.
* Monitor inventory efficiency and stock movement.
* Reduce procurement risks through vendor contribution analysis.
* Support data-driven decision making using KPI-based performance measurement.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure MySQL Database

Update database credentials in the connection file.

### 3️⃣ Execute SQL Queries

Run SQL scripts to extract and combine data from source tables.

### 4️⃣ Run Analysis Notebook

```bash
jupyter notebook
```

### 5️⃣ Execute Analysis Workflow

Run all notebook cells to perform:

* Data Extraction
* Data Cleaning
* KPI Calculation
* Exploratory Data Analysis
* Vendor Performance Analysis
* Visualization Generation

---

## 👨‍💻 Author

**Chetan Malkhed**

Data Analyst | SQL | Python | Business Intelligence Enthusiast


