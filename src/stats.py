import logging
import pandas as pd

logger = logging.getLogger(__name__)

def correlation_analysis(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.Series:
    try:
        return df1.T.corrwith(df2.T, method="pearson")
    except Exception as e:
        logger.error(f"correlation_analysis: Unexpected error: {e}")
        
def linear_regression():
    print("l")

def time_series_decompose():
    print("t")

def growth_rate_analysis():
    print("g")

def rolling_statistics():
    print("r")
    
def clustering():
    print("c")