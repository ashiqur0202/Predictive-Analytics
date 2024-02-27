import pandas as pd
from datetime import timedelta

def add_churn_column(df_engineered, churn_window_days=90):
    """
    Add a 'churn' column to the DataFrame based on the calculated churn date.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with 'txn_date' column.
    - churn_window_days (int): Number of days to consider for churn (default is 90).

    Returns:
    - pd.DataFrame: DataFrame with the added 'churn' column.
    """


    # Convert 'txn_date' to datetime format if not already
    df_engineered['txn_date'] = pd.to_datetime(df_engineered['txn_date'])

    # Sort the DataFrame by 'txn_date'
    df_engineered = df_engineered.sort_values(by='txn_date')

    # Calculate the hypothetical churn date
    last_txn_date = df_engineered['txn_date'].max()
    churn_date = last_txn_date - timedelta(days=churn_window_days)

    # Create 'churn' column based on the calculated churn date
    df_engineered['churn'] = (df_engineered['txn_date'] <= churn_date).astype(int)
    return df_engineered
