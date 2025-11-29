
# DAX Measures for Sales & Profit Analytics Dashboard

-- Basic Metrics
Total Sales = SUM(Sales[Sales])

Total Profit = SUM(Sales[Profit])

Total Orders = DISTINCTCOUNT(Sales[Order ID])

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

-- Time Intelligence
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))

YoY Sales Growth % = DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0)

Sales MTD = TOTALMTD([Total Sales], 'Date'[Date])

Sales QTD = TOTALQTD([Total Sales], 'Date'[Date])

Sales YTD = TOTALYTD([Total Sales], 'Date'[Date])

-- Customer Metrics
Unique Customers = DISTINCTCOUNT(Sales[Customer Name])

Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)

Repeat Customers = 
VAR TotalCust = DISTINCTCOUNT(Sales[Customer Name])
VAR Repeat = CALCULATE(DISTINCTCOUNT(Sales[Customer Name]), FILTER(VALUES(Sales[Customer Name]), CALCULATE(COUNTROWS(Sales)) > 1))
RETURN DIVIDE(Repeat, TotalCust, 0)

-- Product
Top 10 Products Sales = 
CALCULATE([Total Sales], TOPN(10, VALUES(Sales[Product Name]), [Total Sales]))

-- Profitability checks
Loss Making Orders = CALCULATE(COUNTROWS(Sales), FILTER(Sales, Sales[Profit] < 0))
