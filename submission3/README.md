# DSCI 510 Final Project: Investigating the Relationship Between Gas Prices, EV sales, and CO2 Emissions
# Author: Ran Tao

This repository contains the work done for DSCI 510, investigating the relationship between gas prices, Electric Vehicle (EV) sales, and CO2 emissions from transportation.

# Project Motivation
With the growing concern over climate change and its impacts, finding ways to reduce greenhouse gas emissions has become a top priority. Transportation, particularly vehicles powered by gasoline or diesel fuel, is one of the major contributors to these emissions. EVs have emerged as a promising alternative, offering lower emissions and reduced dependency on fossil fuels.

This project aims to understand the factors that influence consumer behavior and the market demand for EVs. Specifically, we aim to investigate the relationship between gas prices, EV sales, and CO2 emissions, and how these factors can be leveraged to achieve a more sustainable and low-carbon transportation system.

# Data Sources
The project’s data source consists of three components:

Weekly U.S. All Grades All Formulations Retail Gasoline Prices (Dollars per Gallon) from 1993 to the present day, obtained via web scraping from [this website](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epm0_pte_nus_dpg&f=w) ↗.

CO2 emission data obtained from a free API created by the US government. The data includes CO2 emissions by year, state, sector, and fuel type. More details can be found [here](https://www.eia.gov/opendata/browser/co2-emissions/co2-emissions-aggregates?frequency=annual&data=value;&facets=stateId;sectorId;fuelId;&stateId=CA;&sectorId=TC;&fuelId=NG;&sortColumn=period;&sortDirection=desc;) ↗.

The number of electric cars for each year, obtained from [this website](https://www.bts.gov/content/gasoline-hybrid-and-electric-vehicle-sales) ↗.

# Analysis and Results
Three separate analyses were conducted using linear regression models:

A strong positive correlation was found between gas prices and the number of electric cars. This suggests that as gas prices increase, more people may be willing to adopt electric cars.

A strong negative correlation was found between CO2 emission and the number of electric cars. This suggests that electric cars can significantly contribute to reducing CO2 emissions.

A multiple linear regression model revealed that both gas price and CO2 emission are important predictors of the adoption of electric cars. Specifically, an increase in gas price led to an increase in the adoption of electric cars, while an increase in CO2 emission led to a decrease in the adoption of electric cars.

These findings highlight the potential for electric cars to play a critical role in promoting sustainable transportation and reducing greenhouse gas emissions.

# Implications
Policymakers and industry leaders can use these results to develop effective strategies to promote the adoption of electric cars, such as implementing incentives for consumers to purchase electric cars or investing in infrastructure to support electric vehicle charging.

# Contact
For any inquiries or further discussion related to this project, please feel free to contact Ran Tao at [email address].
