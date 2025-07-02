"""
main.py

Description:
    A global economic indicators dashboard.

Author:
    Erik Straight <estraight1264@gmail.com>

Created:
    2025-06-27

Python Version:
    3.11.9

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
from src.stats import correlation_analysis, linear_regression_statsmodels, time_series_decomposition, growth_rate_analysis, rolling_statistics, linear_regression_sklearn
from src.plot_stats import plot_correlations, plot_time_series_decomposition, plot_growth_rate_analysis, plot_rolling_statistics
from src.export_utils import export_correlation_to_csv, export_linear_regression_sklearn_table, export_linear_regression_statsmodels_table
from src.analysis_utils import format_stats_as_dataframe

os.makedirs("logs", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("output", exist_ok=True)

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
        # Import GDP data
        gdp = load_data(gdp_csv_loc)
        logging.info(f"Loaded raw data from {gdp_csv_loc}")
        
        # Import inflation data
        inflation = load_data(inflation_csv_loc)
        logging.info(f"Loaded raw data from {inflation_csv_loc}")
        
        # Clean GDP data
        gdp = clean_data(gdp)
        logging.info(f"Cleaned data from set {gdp_csv_loc}")
        
        # Clean inflation data
        inflation = clean_data(inflation)
        logging.info(f"Cleaned data from set {inflation_csv_loc}")        
        
        # Set the indices for each DataFrame to 'Country Name'
        gdp = set_country_index(gdp)
        inflation = set_country_index(inflation)
        
        # Slice each DataFrame for a specific sample of the data
        gdp_mini = slice_dataframe(gdp, COUNTRIES, START_YEAR, END_YEAR)
        inflation_mini = slice_dataframe(inflation, COUNTRIES, START_YEAR, END_YEAR)

        # Plot the GDP on a line graph
        # gdp_plot = prepare_plot_data(gdp, COUNTRIES, str(START_YEAR), str(END_YEAR))
        # plot_gdp_trends(gdp_plot, COUNTRIES, years)
        
        # # Generate correlation analysis data for GDP and inflation and export to CSV and a bar chart .png file
        # gdp_inflation_correlation_analysis = correlation_analysis(gdp_mini, inflation_mini)
        # export_correlation_to_csv(gdp_inflation_correlation_analysis)
        # plot_correlations(gdp_inflation_correlation_analysis, title="GDP and Inflation Correlation")
        
        # Linear regression
        # lm = linear_regression_sklearn(gdp_mini, inflation_mini)
        # export_linear_regression_sklearn_table(lm, "output/lm_sklearn.txt")
        
        
        # Time series decompose
        # countries_decomp = ["United States", "Russian Federation", "Ireland"]
        # decomposition_result = time_series_decomposition(gdp, countries_decomp, "2000", "2023")
        # plot_time_series_decomposition(decomposition_result, countries_decomp)
        
        # Growth rate analysis
        # growth_rates = growth_rate_analysis(gdp, ["Ireland", "United States"], str(START_YEAR), str(END_YEAR))
        # plot_growth_rate_analysis(growth_rates, list(range(START_YEAR, END_YEAR)))
        
        # Rolling statistics
        # rolling_stats = rolling_statistics(gdp, ["Ireland"], str(START_YEAR), str(END_YEAR), 4)
        # formatted_rolling_stats = format_stats_as_dataframe(rolling_stats)
        # plot_rolling_statistics(formatted_rolling_stats)
        
    except Exception as e:
        logging.error(f"Fatal error in main pipeline: {e}", exc_info=True)
    
if __name__ == "__main__":
    main()