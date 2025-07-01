import logging
import pandas as pd

logger = logging.getLogger(__name__)

def slice_dataframe(df: pd.DataFrame, countries: list, start_year: str, end_year: str) -> pd.DataFrame:
    try:
        return df.loc[countries, str(start_year):str(end_year)].copy()
    except Exception as e:
        logger.error(f"slice_dataframe: Unexpected error: {e}")
        
def prepare_plot_data(df: pd.DataFrame, countries: list, start_year: str, end_year: str):
    """
        Prepare data for matplotlib

    Args:
        df (pd.DataFrame): Pandas dataframe.
        countries (list): The desired countries to view in the graph.
        start_year (str): The first year to start with
        end_year (str): The last year to graph 

    Returns:
        pd.DataFrame: A new dataframe prepped for matplotlib.
    """
    try:
        df_plot = df.loc[countries, start_year:end_year].copy()
        df_plot.columns = [int(col) for col in df_plot.columns]
        return df_plot
    except KeyError as e:
        logger.error(f"prepare_plot_data: Could not find specified countries or year range: {e}")
        raise
    except ValueError as e:
        logger.error(f"prepare_plot_data: Failed to convert column names to integers: {e}")
        raise
    except Exception as e:
        logger.error(f"prepare_plot_data: Unexpected error {e}")
        raise

def set_country_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Set the index of a dataframe to the country column

    Args:
        df (pd.DataFrame): Pandas dataframe.

    Returns:
        pd.DataFrame: A new dataframe with the index changed to countries.
    """
    try:
        if "Country Name" not in df.columns:
            raise ValueError("'Country Name' not found in column DataFrame")
    
        return df.set_index("Country Name")
    
    except ValueError as e:
        logger.error(f"set_country_index: {e}")
        raise
    except Exception as e:
        logger.error(f"set_country_index: Unexpected error: {e}")
        raise
