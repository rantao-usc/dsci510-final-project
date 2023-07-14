The scraper.py file uses the beautifulsoup4 library to scrape data from a table on the website: https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epm0_pte_nus_dpg&f=a. The expected output data consists of the year and the gas price for that year.

To make the scraper.py program more user-friendly, we use the argparse library to handle command-line arguments. The program can be run with three different inputs:

1. scraper.py - Running the script without any arguments will print the complete scraped dataset to standard output as rows of data.

2. scraper.py --scrape N - Running the script with the --scrape flag followed by an integer value N will print the first N entries of the dataset to standard output.

3. scraper.py --save <path_to_dataset> - Running the script with the --save flag followed by a file path path_to_dataset will save the complete scraped dataset to the specified file path. 

For example, 
scraper.py --save my_scraped_data.csv will save the dataset to a file called my_scraped_data.csv, and scraper.py --save dir1/dir2/football_stats.csv will save the dataset to a file called football_stats.csv in the dir2 directory inside the dir1 directory. Note that <path_to_dataset> is just a placeholder for the actual file path.
