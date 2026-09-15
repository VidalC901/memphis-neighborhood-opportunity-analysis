Memphis Neighborhood Opportunity Analysis

An end-to-end data analytics project analyzing income, employment,
poverty, housing affordability, and homeownership across census tracts
in Shelby County, Tennessee using U.S. Census American Community Survey
(ACS) data.

The project demonstrates a complete analytics workflow from API data
collection and cleaning to exploratory analysis, SQL-based analysis, and
interactive Power BI visualization.

Project Overview

This project analyzes socioeconomic and housing conditions across census
tracts in Shelby County, Tennessee.

The goal is to identify differences in economic opportunity and housing
conditions between neighborhoods and highlight census tracts
experiencing higher levels of economic hardship or housing burden.

The analysis uses data from the U.S. Census Bureau American Community
Survey (ACS) 5-Year Estimates and combines Python, pandas, SQL, and
Power BI into an end-to-end analytics workflow.

Business Questions

The analysis focuses on several questions:

Which census tracts have the highest and lowest household incomes?

Which census tracts experience the highest poverty rates?

Which census tracts have the highest unemployment rates?

How does poverty relate to unemployment across census tracts?

Which census tracts have the greatest housing cost burden?

How does household income compare with median gross rent?

Which census tracts have higher or lower homeownership rates?

Which neighborhoods show indicators of greater combined economic
hardship?

Data Source

The project uses the U.S. Census Bureau American Community Survey
(ACS) 5-Year Estimates.

Geographic Scope

State: Tennessee

County: Shelby County

State FIPS: 47

County FIPS: 157

Dataset: ACS 5-Year Estimates

Year: 2024

The Census API was used to retrieve demographic, income, employment,
poverty, and housing variables at the census-tract level.

Key Variables

The analysis includes variables such as:

Total population

Median age

Median household income

Poverty population

Civilian labor force

Unemployed population

Occupied housing units

Owner-occupied housing units

Renter-occupied housing units

Median gross rent

Median home value

Several additional metrics were derived from these variables, including:

Poverty rate

Unemployment rate

Homeownership rate

Rent-to-income percentage

Analysis Workflow

The project follows an end-to-end data analytics workflow:

U.S. Census ACS API
        ↓
Python / Requests
        ↓
Data Cleaning with pandas
        ↓
Processed Dataset
        ↓
SQL Analysis
        ↓
Exploratory Analysis
        ↓
Power BI Dashboard
        ↓
Business Insights

1. Data Collection

Python and the Census API were used to retrieve ACS data for Shelby
County census tracts.

2. Data Cleaning

The raw Census data was processed using Python and pandas.

Cleaning and preparation included:

Renaming variables

Converting numeric fields

Handling missing values

Creating derived metrics

Preparing the dataset for analysis

3. Exploratory Analysis

A Jupyter notebook was used to examine the structure and quality of the
dataset and explore relationships between socioeconomic variables.

The final processed dataset contains 249 census tracts and 21
columns.

4. SQL Analysis

SQL was used to perform analytical queries against the processed census
data.

Examples include:

Overall dataset statistics

Highest-income census tracts

Lowest-income census tracts

Poverty analysis

Unemployment analysis

Housing affordability analysis

5. Power BI Dashboard

Power BI was used to transform the analysis into an interactive
dashboard.

The dashboard contains three analytical pages:

Opportunity Overview

Housing Affordability

Employment & Poverty

Power BI Dashboard

Opportunity Overview

The Opportunity Overview page provides a high-level view of
socioeconomic conditions across Shelby County census tracts.

It includes comparisons of:

Household income

Poverty

Unemployment

Population

Income groups

Census-tract-level opportunity indicators



Housing Affordability

The Housing Affordability page examines the relationship between
household income, rent, homeownership, and housing burden.

Key dashboard metrics include:

Average household income: approximately $68K

Average median gross rent: approximately $1K

Average homeownership rate: approximately 51.4%

Average rent-to-income percentage: approximately 29.3%

The dashboard also identifies census tracts with higher rent burdens and
compares household income with median rent.



Employment & Poverty

The Employment & Poverty page focuses on indicators of economic
hardship.

Key dashboard metrics include:

Average poverty rate: approximately 20.9%

Average unemployment rate: approximately 8.6%

Average household income: approximately $67.7K

Total population represented: approximately 919K

The page includes comparisons between poverty and unemployment and
identifies census tracts with higher poverty and unemployment rates.



Key Findings

The analysis highlights several important patterns across Shelby County
census tracts.

Economic Conditions

Household income varies substantially between census tracts, with some
areas having median household incomes well above the county-wide average
while others have considerably lower incomes.

Poverty and Unemployment

The dashboard shows a positive relationship between poverty and
unemployment rates across census tracts. Census tracts with higher
poverty rates frequently also show higher unemployment rates.

The highest-poverty census tracts identified by the dashboard have
poverty rates substantially above the overall average.

Housing Affordability

Housing burden varies considerably between census tracts. Some census
tracts have rent-to-income percentages above 50%, indicating that a
significant share of household income may be devoted to rent.

Homeownership

Homeownership also varies substantially across census tracts. The
dashboard's overall average homeownership rate is approximately 51.4%,
while individual census tracts show considerably different ownership
levels.

Neighborhood-Level Differences

The analysis demonstrates that socioeconomic conditions can vary
significantly between census tracts. Looking at county-wide averages
alone can hide important neighborhood-level differences in income,
employment, poverty, and housing affordability.

Project Structure

memphis-neighborhood-opportunity-analysis/
│
├── dashboard/
│   ├── memphis_neighborhood_opportunity_analysis.pbix
│   └── README.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── images/
│   ├── opportunity_overview.png
│   ├── housing_affordability.png
│   └── employment_poverty.png
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── src/
│   ├── clean_data.py
│   ├── database.py
│   └── download_census_data.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

How to Reproduce the Analysis

1. Clone the repository

git clone https://github.com/VidalC901/memphis-neighborhood-opportunity-analysis.git
cd memphis-neighborhood-opportunity-analysis

2. Create a Python virtual environment

python -m venv .venv

Activate it on Linux/WSL:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure the Census API

Create a .env file based on .env.example.

CENSUS_API_KEY=your_api_key_here

The API key is stored in the local environment and is intentionally
excluded from Git using .gitignore.

5. Download the Census data

Run:

python src/download_census_data.py

This retrieves the selected ACS variables for Shelby County census
tracts.

6. Clean and process the data

Run:

python src/clean_data.py

The processed dataset is saved in the data/processed/ directory.

7. Run the exploratory analysis

Open:

notebooks/01_exploratory_analysis.ipynb

Run the notebook to reproduce the exploratory analysis.

8. Run the SQL analysis

The SQL scripts in sql/ contain the table creation and analytical
queries used throughout the project.

sql/create_tables.sql
sql/analysis_queries.sql

9. Open the Power BI dashboard

Open the .pbix file located in:

dashboard/

The dashboard contains the three analytical pages shown above.

Technologies & Skills Demonstrated

Programming & Data Analysis

Python

pandas

Requests

Jupyter Notebook

Data cleaning

Exploratory data analysis

Data transformation

Derived metrics

SQL

SQL querying

Table creation

Aggregations

Filtering

Sorting

Analytical queries

Working with structured datasets

Data Visualization

Microsoft Power BI

KPI cards

Bar charts

Scatter plots

Tables

Top-N analysis

Dashboard design

Interactive filtering

Data Engineering

REST API data collection

Environment variables

Raw vs. processed data organization

Reproducible data pipelines

Structured project organization

Analytical Skills

Business question development

Socioeconomic analysis

Housing affordability analysis

Poverty and unemployment analysis

Neighborhood-level comparison

Translating data into business insights

Skills Demonstrated

This project demonstrates the ability to take a dataset from raw API
data to a finished business intelligence dashboard.

The project combines:

Data Collection → Data Cleaning → Exploratory Analysis → SQL →
Visualization → Business Insights

This workflow reflects a practical data analyst workflow and
demonstrates experience working with real-world public data rather than
a pre-cleaned dataset.

Data Source

U.S. Census Bureau --- American Community Survey (ACS) 5-Year
Estimates

The Census Bureau provides publicly available demographic, economic,
housing, and social statistics used in this analysis.

Author

Vidal Calderon

Computer Science graduate building projects focused on software
development, data analytics, and modern technology.
