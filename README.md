# Sales & Profit Analytics Dashboard

**Project generated:** 2025-11-29 07:56 UTC

This repository contains a complete working project for a **Power BI - Sales & Profit Analytics Dashboard**. It includes a synthetic dataset, step-by-step instructions to build the PBIX file, DAX measures, and sample chart images you can use as screenshots for your GitHub README.

## What is included
- `dataset.xlsx` - Sales, Region and Date tables (ready to import into Power BI)
- `DAX_measures.md` - All DAX measures used in the project
- `Report_layout.md` - Step-by-step layout to create pages, visuals & interactions in Power BI
- `README.md` - This file
- `sample_charts/` - Three sample PNG charts (for README / preview)
- `project_zip.zip` - A zip of the whole project (for upload)

## How to use
1. Download `dataset.xlsx` and open Power BI Desktop.
2. Get Data → Excel → select `dataset.xlsx` and load tables.
3. Create relationships: Sales[Order Date] → Date[Date], Sales[State] → Region[State].
4. Follow `Report_layout.md` for building pages and visuals, and add measures from `DAX_measures.md`.
5. Use sample PNGs as preview images for your GitHub repository.

## Notes
- This dataset is synthetic and generated for learning/portfolio purposes.
- I could not create a `.pbix` file (Power BI Desktop is required). The included files contain everything you need to build the report quickly in Power BI Desktop.
