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

import os
import logging
from src.load_data import load_data
from src.clean_data import clean_data
from src.data_helpers import prepare_plot_data, set_country_index, slice_dataframe
from src.plot_gdp import plot_gdp_trends
from src.stats import correlation_analysis
from src.plot_stats import plot_correlations

os.makedirs("logs", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

def main():
    COUNTRIES = ["United States", "China", "Russian Federation", "Germany",
                 "France", "United Kingdom", "Japan", "Iran, Islamic Rep.", "Ireland"]
    START_YEAR = 2000
    END_YEAR = 2023
    years = list(range(START_YEAR, END_YEAR + 1))
    gdp_csv_loc = "./data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_127285.csv"
    inflation_csv_loc = "./data/Inflation/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_127296.csv"
    
    try:
        gdp = load_data(gdp_csv_loc)
        logging.info(f"Loaded raw data from {gdp_csv_loc}")
        
        inflation = load_data(inflation_csv_loc)
        logging.info(f"Loaded raw data from {inflation_csv_loc}")
        
        gdp = clean_data(gdp)
        logging.info(f"Cleaned data from set {gdp_csv_loc}")
        
        inflation = clean_data(inflation)
        logging.info(f"Cleaned data from set {inflation_csv_loc}")        
        
        gdp = set_country_index(gdp)
        inflation = set_country_index(inflation)
        
        gdp_mini = slice_dataframe(gdp, COUNTRIES, START_YEAR, END_YEAR)
        inflation_mini = slice_dataframe(inflation, COUNTRIES, START_YEAR, END_YEAR)

        gdp_plot = prepare_plot_data(gdp, COUNTRIES, str(START_YEAR), str(END_YEAR))
        
        plot_gdp_trends(gdp_plot, COUNTRIES, years)
        
        gdp_inflation_correlation_analysis = correlation_analysis(gdp_mini, inflation_mini)
        print(gdp_inflation_correlation_analysis)
        gdp_inflation_correlation_analysis.name = "Correlation Coefficient"
        gdp_inflation_correlation_analysis.to_csv("outputs/correlation_results.csv", header=True)
        
        plot_correlations(gdp_inflation_correlation_analysis, title="GDP and Inflation Correlation")
        
    except Exception as e:
        logging.error(f"Fatal error in main pipeline: {e}", exc_info=True)
    

if __name__ == "__main__":
    main()