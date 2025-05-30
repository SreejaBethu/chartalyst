import pandas as pd

def clean_and_describe_data(df: pd.DataFrame) -> str:
    desc = df.describe(include='all').transpose()
    summary = f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.\n"
    summary += f"Columns: {', '.join(df.columns)}\n"
    summary += str(desc.head())
    return summary
