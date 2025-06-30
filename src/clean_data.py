import logging
import pandas as pd

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataframe assuming the columns are by year. Drops any row missing all year values.
    
    Args:
        df (pd.DataFrame): A pandas dataframe with raw data
        
    Returns:
        df (pd.DataFrame): The cleaned dataframe
    """
    
    try:
        # Extract year columns
        year_columns = [col for col in df.columns if col.isdigit()]
        # Keep only rows with at least one year of data
        df = df.dropna(subset=year_columns, how="all").copy()
        # Convert all year columns to numeric (float)
        df[year_columns] = df[year_columns].apply(pd.to_numeric, errors="coerce")
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
        
    return df