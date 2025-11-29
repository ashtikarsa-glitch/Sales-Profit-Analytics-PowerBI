
# Report Layout & Step-by-step (Power BI)

## Pages
1. Executive Summary
   - Cards: Total Sales, Total Profit, Profit Margin %, Total Orders
   - Line Chart: Sales & Profit over time (Date[Month])
   - Map: Sales by State (use Region table for hierarchy)
   - Bar Chart: Top 10 Products by Profit
   - Table: Bottom 10 Loss Making Products

2. Sales Analysis
   - Area Chart: Monthly Sales Trend (use Date[YearMonth])
   - Stacked Column: Sales by Category & Segment
   - Scatter: Sales vs Discount (add Profit as size)
   - Donut: Category Contribution %

3. Profit Analysis
   - Bar: Profit by Product Subcategory
   - Line: Profit Margin % over time
   - Decomposition Tree: Explore profit by Category -> Subcategory -> Product

4. Customer Analysis
   - Table: Customer Rank by Sales (Top N slicer)
   - KPI: Repeat Customer Rate
   - Clustered Bar: Segment-wise customer count

## Interactions & Filters
- Add slicers: Date range (between), Region, Segment, Category
- Sync slicers across pages for consistent filtering
- Use Drillthrough page for Order-level detail
- Add bookmarks for "QTD View", "YTD View", "Top Products"

## Tips
- Create a Date table and mark as 'Date Table' in Model view
- Set relationships: Sales[Order Date] -> Date[Date]; Sales[State] -> Region[State]
- Use conditional formatting on tables to highlight negative profits
- Use Top N filters for product ranking visuals
