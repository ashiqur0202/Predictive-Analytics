# Data Preprocessing Function
def preprocess_data(data):
    # Droping Unnamed: 0 columns
    data = data.drop(columns="Unnamed: 0")

    # Checking for data integrity
    # For example, ensuring 'txn_date' is in the correct format
    data['txn_date'] = pd.to_datetime(data['txn_date'], errors='coerce')

    # Handling outliers in 'txn_amount'
    Q1 = data['txn_amount'].quantile(0.25)
    Q3 = data['txn_amount'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    data = data[(data['txn_amount'] >= lower_bound) & (data['txn_amount'] <= upper_bound)]

    return data
