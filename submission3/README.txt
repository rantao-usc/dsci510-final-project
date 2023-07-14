This project involved several steps to analyze the relationship between gas prices, CO2 emissions, and the adoption of electric cars. Here is a brief overview of the project:

1. Web scraping: I used Python to web scrape a table from the following website: url = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epm0_pte_nus_dpg&f=a'. I extracted the gas prices for each year and stored them in a CSV file called gas_price.csv.

2. API data retrieval: I retrieved CO2 emission data for each year from the following API: 'https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?api_key=j3dEAAmfxdpvHVe5RumfMXIYEnkVLSPKPDEbo59A&frequency=annual&data[0]=value&facets[stateId][]=CA&facets[sectorId][]=TC&facets[fuelId][]=NG&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'. I stored the data in a CSV file called co2_data.csv.

3. Data download: I downloaded an .xlsx file online and stored it in the datasets directory.

4. Data analysis: I compared the gas price, CO2 emission, and electric car adoption data to analyze the relationship between these variables. Specifically, I conducted the following analyses:

   1. Relationship between gas price and number of electric cars
   2. Relationship between CO2 emission and number of electric cars
   3. Built a linear regression model to predict the number of electric cars using gas price and CO2 emission

Overall, this project provides valuable insights into the factors that influence the adoption of electric cars and can guide policymakers in developing effective strategies to promote sustainable transportation.
