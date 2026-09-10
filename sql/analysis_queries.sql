-- 1. Dataset overview

SELECT
    COUNT(*) AS total_tracts,
    ROUND(AVG(total_population), 0) AS avg_tract_population,
    ROUND(AVG(median_household_income), 2) AS avg_household_income,
    ROUND(AVG(poverty_rate), 2) AS avg_poverty_rate,
    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment_rate,
    ROUND(AVG(homeownership_rate), 2) AS avg_homeownership_rate
FROM census_tract_metrics;

-- 2. Highest-income census tracts

SELECT
    tract_geoid,
    geography_name,
    total_population,
    median_household_income
FROM census_tract_metrics
WHERE
    total_population >= 500
    AND median_household_income IS NOT NULL
ORDER BY median_household_income DESC
LIMIT 10;

-- 3. Lowest-income census tracts

SELECT
    tract_geoid,
    geography_name,
    total_population,
    median_household_income
FROM census_tract_metrics
WHERE
    total_population >= 500
    AND median_household_income IS NOT NULL
ORDER BY median_household_income ASC
LIMIT 10;

-- 4. Highest-poverty census tracts

SELECT
    tract_geoid,
    geography_name,
    total_population,
    median_household_income,
    poverty_rate
FROM census_tract_metrics
WHERE total_population >= 500
ORDER BY poverty_rate DESC
LIMIT 10;

-- 5. Highest-unemployment census tracts

SELECT
    tract_geoid,
    geography_name,
    total_population,
    unemployment_rate,
    poverty_rate
FROM census_tract_metrics
WHERE total_population >= 500
ORDER BY unemployment_rate DESC
LIMIT 10;

-- 6. Highest estimated rent-to-income burden

SELECT
    tract_geoid,
    geography_name,
    median_household_income,
    median_gross_rent,
    ROUND(rent_to_income_ratio * 100, 1) AS rent_to_income_percent
FROM census_tract_metrics
WHERE
    total_population >= 500
    AND rent_to_income_ratio IS NOT NULL
ORDER BY rent_to_income_ratio DESC
LIMIT 10;

-- 7. Identify high-need tracts

SELECT
    tract_geoid,
    geography_name,
    median_household_income,
    poverty_rate,
    unemployment_rate,
    homeownership_rate
FROM census_tract_metrics
WHERE
    total_population >= 500
    AND poverty_rate >= 30
    AND unemployment_rate >= 10
ORDER BY poverty_rate DESC;

-- 8. Compare income groups

SELECT
    CASE
        WHEN median_household_income < 30000 THEN 'Under $30K'
        WHEN median_household_income < 50000 THEN '$30K-$49,999'
        WHEN median_household_income < 75000 THEN '$50K-$74,999'
        WHEN median_household_income < 100000 THEN '$75K-$99,999'
        ELSE '$100K+'
    END AS income_group,

    COUNT(*) AS tract_count,

    ROUND(AVG(poverty_rate), 2) AS avg_poverty_rate,

    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment_rate,

    ROUND(AVG(homeownership_rate), 2) AS avg_homeownership_rate

FROM census_tract_metrics

WHERE
    total_population >= 500
    AND median_household_income IS NOT NULL

GROUP BY income_group

ORDER BY
    MIN(median_household_income);

-- 9. Compare high-poverty tracts to county tract averages

WITH county_averages AS (
    SELECT
        AVG(poverty_rate) AS avg_poverty_rate,
        AVG(unemployment_rate) AS avg_unemployment_rate,
        AVG(homeownership_rate) AS avg_homeownership_rate
    FROM census_tract_metrics
    WHERE total_population >= 500
)

SELECT
    c.tract_geoid,
    c.geography_name,
    c.poverty_rate,
    c.unemployment_rate,
    c.homeownership_rate,

    ROUND(
        c.poverty_rate - a.avg_poverty_rate,
        2
    ) AS poverty_points_above_average,

    ROUND(
        c.unemployment_rate - a.avg_unemployment_rate,
        2
    ) AS unemployment_points_above_average

FROM census_tract_metrics AS c
CROSS JOIN county_averages AS a

WHERE
    c.total_population >= 500
    AND c.poverty_rate > a.avg_poverty_rate

ORDER BY
    poverty_points_above_average DESC

LIMIT 10;
