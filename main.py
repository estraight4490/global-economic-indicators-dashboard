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
    - numpy
    - matplotlib
    (or just say: see requirements.txt)

Usage:
    python main.py

Notes:
    - Any setup instructions
    - TODOs
    - Known limitations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gdp = pd.read_csv("./data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_127285.csv", skiprows=4)
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
