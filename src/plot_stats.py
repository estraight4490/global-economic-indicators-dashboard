
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
import pandas as pd
import logging
from statsmodels.tsa.seasonal import DecomposeResult

logger = logging.getLogger(__file__)

DIR = "figures/"

# TODO: Decide output_path and filename handling
def plot_correlations(correlations: pd.Series, title: str = "Correlation", output_path: str = "figures/correlation_plot.png"):
    """
    Plots a horizontal bar chart of correlation coefficients by country.
    
    Args:
        correlation (pd.Series): Series of correlation values (index: countries).
        title (str): Title for the chart.
        output_path (str): File path to save the chart.
    """
    try:
        filename = f"{title.replace(' ', '_').lower()}_plot.png"
        correlations = correlations.sort_values()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=correlations.values,
            y=correlations.index,
            hue=correlations.index,
            dodge=False,
            palette="coolwarm",
            legend=False
        )
        plt.xlabel("Correlation Coefficient")
        plt.title(title)
        plt.axvline(0, color="gray", linestyle="--")
        plt.tight_layout()
        plt.savefig(DIR + filename, bbox_inches="tight")
        plt.show()
    except Exception as e:
        logger.error(f"plot_correlations: Unexpected error: {e}")
        

def plot_time_series_decomposition(results: list[DecomposeResult], countries: list[str]):
    if(len(results) != len(countries)):
        raise ValueError("Lists must be the same length")
    
    for country, result in zip(countries, results):
        result.plot()
        plt.suptitle(f"Time Series Decomposition of GDP - {country}", fontsize=16)
        plt.tight_layout()
        plt.savefig(f"{DIR}decomposition_results_{country}.png", bbox_inches="tight")
        plt.show()
        
def plot_growth_rate_analysis(countries_growth_rates: dict, years: list[int]) -> None:
    for country in countries_growth_rates:
        growth_rates = countries_growth_rates[country]
        plt.plot(years, growth_rates, label=country)

    plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=100))
    plt.title("Growth Rate Analysis (Current US$)")
    plt.ylabel("Growth Rate")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("figures/growth_rate_analysis.png", bbox_inches="tight")
    plt.show()
        
        