from sklearn.model_selection import GridSearchCV

def tune_hyperparameters(base_model, param_grid, X_train, y_train):
    # Initialize Grid Search with the base model and parameter grid
    grid_search = GridSearchCV(base_model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

    # Fit the grid search to the data
    grid_search.fit(X_train, y_train)

    # Get the best-tuned model
    tuned_model = grid_search.best_estimator_

    return tuned_model

# Example parameter grid for RandomForestClassifier
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Assuming X_train and y_train are obtained from the split_data function
# Assuming trained_model is the initial RandomForest model trained in your previous step
tuned_model_rf = tune_hyperparameters(trained_model, param_grid_rf, X_train, y_train)

# Now you can use tuned_model_rf for evaluation or further steps
