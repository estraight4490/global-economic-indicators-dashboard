
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging

logger = logging.getLogger(__file__)

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
        dir = "figures/"
        filename = f"{title.replace(" ", "_").lower()}_plot.png"
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
        plt.savefig(dir + filename, bbox_inches="tight")
        plt.show()
    except Exception as e:
        logger.error(f"plot_correlations: Unexpected error: {e}")
        
