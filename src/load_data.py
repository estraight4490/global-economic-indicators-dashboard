import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_data(csv_file_loc, skip_rows=4):
    """
    Load raw data from a csv and return the data.

    Args:
        csv_file_loc (String): The name and path of the csv file loaded.
        skiprows(Number): The number of rows to skip at the beginning of the csv file. The default is 4.

    Returns:
        pd.DataFrame: Dataframe containing raw data loaded into memory.
    """
    try:
       df = pd.read_csv(csv_file_loc, skiprows=skip_rows)
       logger.info("Loading raw data")
    except FileNotFoundError as e:
        logger.error(f"Error: {e}")
        df = None
        
    return df