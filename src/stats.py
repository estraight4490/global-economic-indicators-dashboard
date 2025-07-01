import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose, DecomposeResult
import warnings
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def correlation_analysis(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.Series:
    try:
        return df1.T.corrwith(df2.T, method="pearson")
    except Exception as e:
        logger.error(f"correlation_analysis: Unexpected error: {e}")

# TODO: Refactor
def linear_regression(X: pd.DataFrame, y: pd.DataFrame, output_path: str = "output/linear_regression_report.txt") -> None:
    model = LinearRegression()
    
    X_copy = X.copy().apply(pd.to_numeric, errors="coerce").interpolate(axis=1, limit_direction="both")
    y_copy = X.copy().apply(pd.to_numeric, errors="coerce").interpolate(axis=1, limit_direction="both")
    
    output_lines = []
    
    for country in X_copy.index:
        x_vals = X_copy.loc[country].values
        y_vals = y_copy.loc[country].values
        
        # Reshape for sklearn
        x_vals_2d = x_vals.reshape(-1, 1)
        model.fit(x_vals_2d, y_vals)
        y_pred = model.predict(x_vals_2d)
        
        r2 = r2_score(y_vals, y_pred)
        mse = mean_squared_error(y_vals, y_pred)
        
        output_lines.append(f"{country}:\n")
        output_lines.append(f"  Slope     = {model.coef_[0]:.3f}\n")
        output_lines.append(f"  Intercept = {model.intercept_:.2f}\n")
        output_lines.append(f"  R² Score  = {r2:.3f}\n")
        output_lines.append(f"  MSE       = {mse:.2f}\n")

        # statsmodels summary (with warnings suppressed)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                sm_X = sm.add_constant(x_vals)
                sm_model = sm.OLS(y_vals, sm_X).fit()
                output_lines.append(sm_model.summary().as_text())
        except Exception as e:
            output_lines.append(f"  Statsmodels OLS failed: {e}\n")
        
    # Write to file
    with open(output_path, "w") as f:
        f.writelines(output_lines)
        
    logger.info(f"Regression report written to: {output_path}")


def time_series_decomposition(df: pd.DataFrame, country: str, start_date: str, end_date: str) -> DecomposeResult:
    gdp_series = df.loc[country, start_date:end_date].astype(float)
    gdp_series.index = pd.to_datetime(gdp_series.index, format="%Y")
    return seasonal_decompose(gdp_series, model="additive", period=1)

def growth_rate_analysis():
    print("g")

def rolling_statistics():
    print("r")
    
def clustering():
    print("c")