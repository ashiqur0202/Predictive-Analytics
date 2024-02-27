from sklearn.ensemble import RandomForestClassifier

def train_model(model, X_train, y_train):
    # Train the model
    model.fit(X_train, y_train)

    return model