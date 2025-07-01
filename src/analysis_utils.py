
import pandas as pd

def format_stats_as_dataframe(rolling_stats: dict) -> pd.DataFrame:
    rows = []
    for country, stats_dict in rolling_stats.items():
        years = stats_dict["mean"].index
        
        for year in years:
            row = {
                "Country": country,
                "Year": year
            }
            for stat_name, series in stats_dict.items():
                row[stat_name.capitalize()] = series.loc[year]
            rows.append(row)

    return pd.DataFrame(rows)
 