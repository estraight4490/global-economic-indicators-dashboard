"""
main.py

Description:
    A global economic indicators dashboard.

Author:
    Erik Straight <estraight1264@gmail.com>

Created:
    2025-06-27

Python Version:
    3.13.5

Dependencies:
    - pandas
    - matplotlib
    - seaborn

Usage:
    python main.py

Notes:
    - Any setup instructions
    - TODOs
    - Known limitations
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.load_data import load_data
from src.clean_data import clean_data
from src.data_helpers import prepare_plot_data, set_country_index
from src.plot_gdp import plot_gdp_trends

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

def main():
    gdp_csv_loc = "./data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_127285.csv"
    COUNTRIES = ["United States", "China", "Russian Federation", "Germany",
                 "France", "United Kingdom", "Japan", "Iran, Islamic Rep.", "Ireland"]
    START_YEAR = 2000
    END_YEAR = 2023
    years = list(range(START_YEAR, END_YEAR + 1))

    gdp = load_data(gdp_csv_loc)
    logging.info(f"Loaded raw data from {gdp_csv_loc}")
    
    gdp = clean_data(gdp)
    logging.info(f"Cleaned data from set {gdp_csv_loc}")
    
    gdp = set_country_index(gdp)

    gdp_plot = prepare_plot_data(gdp, COUNTRIES, str(START_YEAR), str(END_YEAR))
    
    plot_gdp_trends(gdp_plot, COUNTRIES, years)
    

if __name__ == "__main__":
    main()