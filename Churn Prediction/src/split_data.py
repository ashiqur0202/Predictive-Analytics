from sklearn.model_selection import train_test_split

features = df_churned[['account_number', 'txn_amount', 'txn_month',
       'txn_day', 'txn_type_add_money', 'txn_type_cash_in',
       'txn_type_cash_out', 'txn_type_payment', 'txn_type_send_money',
       'churn']]

target = 'churn'

def split_data(data, target_column='churn'):
    # Extract features and target variable
    X = data.drop(target_column, axis=1)  # Assuming 'churn' is the target column
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
