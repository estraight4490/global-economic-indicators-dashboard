import logging 
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def plot_gdp_trends(df: pd.DataFrame, countries: list[int], years: list[int]) -> None:
    try:   
        for country in countries:
            gdp_values = df.loc[country, years].astype(float)
            plt.plot(years, gdp_values, label=country)
        
        plt.title("GDP Trends (Current US$)")
        plt.ylabel("GDP")
        plt.xlabel("Year")
        plt.xticks(rotation=45)
        plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
        plt.savefig("figures/gdp_trends.png", bbox_inches="tight")
        plt.show()
    except KeyError as e:
        logger.error(f"Key error while plotting GDP trends: {e}")
    except FileNotFoundError as e:
        logger.error(f"Save path issue: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in plot_gdp_trends: {e}")