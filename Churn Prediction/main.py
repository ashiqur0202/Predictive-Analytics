
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# Other necessary imports...
from src.load_data import load_data
from src.preprocess_data import preprocess_data
from src.feature_engineering import feature_engineering
from src.add_churn_column import add_churn_column
from src.split_data import split_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model

def main():
    pd, np, plt, sns, train_test_split, StandardScaler, RandomForestClassifier, accuracy_score, confusion_matrix, classification_report = import_churn_libraries()

    
    # Load data
    file_path = "data/raw/new_raw.csv"  
    data = load_data(file_path)

    # Preprocess data
    preprocessed_data = preprocess_data(data)

    # Feature engineering
    engineered_data = feature_engineering(preprocessed_data)
    
    # Add 'churn' column
    df_churned = add_churn_column(engineered_data)
    
    features = df_churned[['account_number', 'txn_amount', 'txn_month',
       'txn_day', 'txn_type_add_money', 'txn_type_cash_in',
       'txn_type_cash_out', 'txn_type_payment', 'txn_type_send_money',
       'churn']]

    target = 'churn'
    
    # Split data    
    X_train, X_test, y_train, y_test = split_data(features)

    # Choose and train the model
    model = RandomForestClassifier(random_state=42)
    trained_model = train_model(model, X_train, y_train)

    # Evaluate the model
    accuracy, conf_matrix, class_report = evaluate_model(trained_model, X_test, y_test)

    # Display results
    print(f"Model Accuracy: {accuracy}")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nClassification Report:")
    print(class_report)

if __name__ == "__main__":
    main()
