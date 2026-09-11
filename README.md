# Memphis Neighborhood Opportunity Analysis

An end-to-end data analytics project analyzing income, employment, poverty, housing affordability, and homeownership across census tracts in Shelby County, Tennessee using U.S. Census American Community Survey (ACS) data.

The project demonstrates a complete analytics workflow from API data collection and cleaning to exploratory analysis, SQL-based analysis, and interactive Power BI visualization.

---

## Project Overview

This project analyzes socioeconomic and housing conditions across census tracts in Shelby County, Tennessee.

The goal is to identify differences in economic opportunity and housing conditions between neighborhoods and highlight census tracts experiencing higher levels of economic hardship or housing burden.

The analysis uses data from the **U.S. Census Bureau American Community Survey (ACS) 5-Year Estimates** and combines Python, pandas, SQL, and Power BI into an end-to-end analytics workflow.

---

## Business Questions

The analysis focuses on several questions:

- Which census tracts have the highest and lowest household incomes?
- Which census tracts experience the highest poverty rates?
- Which census tracts have the highest unemployment rates?
- How does poverty relate to unemployment across census tracts?
- Which census tracts have the greatest housing cost burden?
- How does household income compare with median gross rent?
- Which census tracts have higher or lower homeownership rates?
- Which neighborhoods show indicators of greater combined economic hardship?

---

## Data Source

The project uses the **U.S. Census Bureau American Community Survey (ACS) 5-Year Estimates**.

### Geographic Scope

- **State:** Tennessee
- **County:** Shelby County
- **State FIPS:** 47
- **County FIPS:** 157
- **Dataset:** ACS 5-Year Estimates
- **Year:** 2024

The Census API was used to retrieve demographic, income, employment, poverty, and housing variables at the census-tract level.

### Key Variables

The analysis includes variables such as:

- Total population
- Median age
- Median household income
- Poverty population
- Civilian labor force
- Unemployed population
- Occupied housing units
- Owner-occupied housing units
- Renter-occupied housing units
- Median gross rent
- Median home value

Several additional metrics were derived from these variables, including:

- Poverty rate
- Unemployment rate
- Homeownership rate
- Rent-to-income percentage

---

## Analysis Workflow

The project follows an end-to-end data analytics workflow:

```text
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
