
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
import pandas as pd
import logging
from statsmodels.tsa.seasonal import DecomposeResult

logger = logging.getLogger(__file__)

DIR = "figures/"

def plot_correlations(correlations: pd.Series, title: str = "Correlation", output_path: str = "figures/correlation_plot.png") -> None:
    """
    Plots a horizontal bar chart of correlation coefficients by country.
    
    Args:
        correlation (pd.Series): Series of correlation values (index: countries).
        title (str): Title for the chart.
        output_path (str): File path to save the chart.
    """
    try:
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
        plt.savefig(output_path, bbox_inches="tight")
        plt.show()
    except Exception as e:
        logger.error(f"plot_correlations: Unexpected error: {e}")
        

def plot_time_series_decomposition(results: list[DecomposeResult], countries: list[str]) -> None:
    """
    Plots a line graph for a time series decomposition.
    
    Args:
        results (list[DecomposeResult]): List of countries' time series data (index: countries).
        countries (list[str]): List of countries' names.
    """
    try:
        if(len(results) != len(countries)):
            raise ValueError("Lists must be the same length")
    
        for country, result in zip(countries, results):
            result.plot()
            plt.suptitle(f"Time Series Decomposition of GDP - {country}", fontsize=16)
            plt.tight_layout()
            plt.savefig(f"{DIR}decomposition_results_{country}.png", bbox_inches="tight")
            plt.show()
            logger.info("plot_time_series_decomposition: Time series decomposition chart generated")
            
    except Exception as e:
        logger.lerror(f"plot_time_series_decomposition: Unexpected error {e}")
        
def plot_growth_rate_analysis(countries_growth_rates: dict, years: list[int]) -> None:
    """
    Plots a line graph for a time series decomposition.
    
    Args:
        countries_growth_rates (dict): Dict of countries' growth rate analysis.
        years (list[str]): The list of years in range of the data.
    """
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
    plt.savefig(f"{DIR}growth_rate_analysis.png", bbox_inches="tight")
    plt.show()

# TODO: Refactor
def plot_rolling_statistics(countries_stats: pd.DataFrame) -> None:
    """
    Plots a line graph for a time series decomposition.
    
    Args:
        countries_growth_rates (dict): Dict of countries' growth rate analysis.
        years (list[str]): The list of years in range of the data.
    """
    years = countries_stats["Year"].tolist()
    
    for country in countries_stats["Country"].unique():
        country_mean_data = countries_stats[countries_stats["Country"] == country]["Mean"]
        plt.plot(years, country_mean_data, label=country)

    plt.title("Rolling Statistics: Mean (Current US$)")
    plt.ylabel("Mean")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(f"{DIR}rolling_statistics_mean.png", bbox_inches="tight")
    plt.show()

    for country in countries_stats["Country"].unique():
        country_std_data = countries_stats[countries_stats["Country"] == country]["Std"]
        plt.plot(years, country_std_data, label=country)

    plt.title("Rolling Statistics: Std. (Current US$)")
    plt.ylabel("Std.")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(f"{DIR}rolling_statistics_std.png", bbox_inches="tight")
    plt.show()
