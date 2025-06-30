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

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

gdp_csv_loc = "./data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_127285.csv"

gdp = load_data(gdp_csv_loc)
logging.info(f"Loaded raw data from {gdp_csv_loc}")
gdp = gdp.set_index("Country Name")
# countries_set_gdp = gdp.loc[["United States", "Germany", "France", "United Kingdom", "Japan", "Iran, Islamic Rep.", "Ireland"], "2000":"2024"].astype("float").plot()

countries = ["United States", "Germany", "France", "United Kingdom", "Japan", "Iran, Islamic Rep.", "Ireland"]
years = [str(y) for y in range(2000, 2024)]

for country in countries:
    gdp_values = gdp.loc[country, years].astype(float)
    plt.plot(years, gdp_values, label=country)
  
plt.title("GDP Trends (Current US$)")
plt.ylabel("GDP")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
