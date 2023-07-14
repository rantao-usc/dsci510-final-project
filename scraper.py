import argparse
import csv
from typing import List, Tuple
import requests
from bs4 import BeautifulSoup


def scrape_data(url: str) -> List[Tuple[str, str]]:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', attrs={'class': 'FloatTitle'})
    data = [] # Initialize an empty list to store the data
    tbody = table.find('tbody')
    body_rows = tbody.find_all('tr')
    for row in body_rows:
        cols = row.find_all('td')
        row_data = []
        for col in cols[1:]:
            if col.text.strip() and col.text.strip() != 'NA': # Check if cell is not empty and not 'NA'
                row_data.append(col.text.strip())
        if row_data: # Ignore empty rows
            data.append(row_data)
    # Combine the data from each row into a single list
    combined_data = []
    for row_data in data:
        combined_data.extend(row_data)
    # Create a list of (year, data) tuples
    years = list(range(1994, 2023))
    year_data = list(zip(years, combined_data))
    return year_data


def print_data(data: List[Tuple[str, str]]) -> None:
    for year, value in data:
        print(f"{year}, {value}")


def print_n_entries(data: List[Tuple[str, str]], n: int) -> None:
    for year, value in data[:n]:
        print(f"{year}, {value}")


def save_data(data: List[Tuple[str, str]], filename: str) -> None:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Data'])
        for year, value in data:
            writer.writerow([year, value])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape and save data from a website.')
    parser.add_argument('--scrape', metavar='N', type=int, help='scrape and print the first N entries of the dataset')
    parser.add_argument('--save', metavar='filename', type=str, help='save the scraped dataset to a CSV file')
    args = parser.parse_args()

    url = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epm0_pte_nus_dpg&f=a'
    year_data = scrape_data(url)

    if args.save:
        save_data(year_data, args.save)
    elif args.scrape:
        print_n_entries(year_data, args.scrape)
    else:
        print_data(year_data)