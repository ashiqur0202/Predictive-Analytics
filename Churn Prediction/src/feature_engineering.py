import pandas as pd

def feature_engineering(df_preprocessed):
    # Extract day from 'txn_date'
    df_preprocessed['txn_day'] = pd.to_datetime(df_preprocessed['txn_date']).dt.day
    
    # Extract month from 'txn_date'
    df_preprocessed['txn_month'] = pd.to_datetime(df_preprocessed['txn_date']).dt.month
    
    # Assuming 'txn_type' is categorical, perform one-hot encoding
    df_preprocessed = pd.concat([df_preprocessed, pd.get_dummies(df_preprocessed['txn_type'], prefix='txn_type').astype(int)], axis=1)

    # Dropping unnecessary columns
    #df_preprocessed = df_preprocessed.drop(['txn_date', 'txn_type'], axis=1)

    return df_preprocessed
