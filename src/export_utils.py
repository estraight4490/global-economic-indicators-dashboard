
import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

def export_correlation_to_csv(correlations: pd.Series, output_path: str = "output/correlation_results.csv") -> None:
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        correlations.name = "Correlation Coefficient"
        correlations.to_csv(output_path, header=True)
        logger.info(f"Correlation results exported to {output_path}")
    except Exception as e:
        logger.error(f"export_correlation_to_csv: Unexpected error: {e}")