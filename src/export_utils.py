
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
        
def write_to_file(output_path: str, output_lines: list):
    # Write to file
    with open(output_path, "w") as f:
        f.writelines(output_lines)
    pass

def export_rolling_stats_to_csv(countries_stats: dict) -> None:
    print("export to csv")
    
def export_linear_regression_sklearn_table(countries_data: dict, output_path: str) -> None:
    output_lines = []
    
    for country, data in countries_data.items():

        slope = data["slope"]
        intercept = data["intercept"]
        r2 = data["r2"]
        mse = data["mse"]

        output_lines.append(f"{country}:\n")
        output_lines.append(f"  Slope     = {slope:.3f}\n")
        output_lines.append(f"  Intercept = {intercept:.2f}\n")
        output_lines.append(f"  R² Score  = {r2:.3f}\n")
        output_lines.append(f"  MSE       = {mse:.2f}\n")
        
    write_to_file(output_path, output_lines)

def export_linear_regression_statsmodels_table(countries_data: dict, output_path: str) -> None:
    output_lines = []
    
    for country in countries_data:
        output_lines.append(f"{country}\n")
        output_lines.append(countries_data[country])
        
    write_to_file(output_path, output_lines)
    