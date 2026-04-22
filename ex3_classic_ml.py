"""
2026_04_24

Classic ML exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.

Objective: Introduction to typical Machine Learning workflow
1) Load train data and test data from a CSV file
2) Fit (train) models on the train data: Linear Regression and Decision Tree
3) Evaluate each model on the test data
4) Compare the evaluation results 
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score,
)
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

###########################
### step 1 - load data from CSV
train_data_filepath = "/home/pfpimenta/python_exercises_unitn/ex3_execution_logs_train.csv"
test_data_filepath = "/home/pfpimenta/python_exercises_unitn/ex3_execution_logs_test.csv"
train_df = pd.read_csv(train_data_filepath)
test_df = pd.read_csv(test_data_filepath)

###########################
### step 2 - Fit (train) models on the train data

### split the data into X and Y
feature_columns = ["matrix_size", "num_threads", "scheduling_type"]
train_X = train_df[feature_columns]
train_Y = train_df["execution_time"]
test_X = test_df[feature_columns]
test_Y = test_df["execution_time"]

### create one-hot-vector out of 'scheduling_type' for the training data
# Initialize the encoder
# handle_unknown='ignore' is a safety net for the test set
ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
# Fit and Transform the training data
scheduling_encoded_train_df = ohe.fit_transform(train_X[["scheduling_type"]])
encoded_cols = ohe.get_feature_names_out()
# Create a DF for the encoded features
train_X_encoded = pd.DataFrame(scheduling_encoded_train_df, columns=encoded_cols, index=train_X.index)
# Merge and drop original
train_X = pd.concat([train_X.drop("scheduling_type", axis=1), train_X_encoded], axis=1)

### 2.a. initalize and fit (train) the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(train_X, train_Y)

### 2.b. initalize and fit (train) the Decision Tree model
dt_model = DecisionTreeRegressor()
dt_model.fit(train_X, train_Y)

###########################
### step 3 - Evaluate each model on the test data

### create one-hot-vector out of 'scheduling_type'
# IMPORTANT: Use ONLY .transform() on the test data
scheduling_encoded_test = ohe.transform(test_X[["scheduling_type"]])
test_X_encoded = pd.DataFrame(scheduling_encoded_test, columns=encoded_cols, index=test_X.index)
# Join and drop original
test_X = pd.concat([test_X.drop("scheduling_type", axis=1), test_X_encoded], axis=1)

# Now you can safely predict
lr_preds = lr_model.predict(test_X)
dt_preds = dt_model.predict(test_X)

###########################
### step 4 - Compare the evaluation results

# Calculate metrics for Linear Regression
lr_mae = mean_absolute_error(test_Y, lr_preds)
lr_mape = mean_absolute_percentage_error(test_Y, lr_preds)
lr_r2 = r2_score(test_Y, lr_preds)

# Calculate metrics for Decision Tree
dt_mae = mean_absolute_error(test_Y, dt_preds)
dt_mape = mean_absolute_percentage_error(test_Y, dt_preds)
dt_r2 = r2_score(test_Y, dt_preds)

# Print results
print("\n" + "=" * 30)
print("MODEL EVALUATION RESULTS")
print("=" * 30)
print(f"Linear Regression:")
print(f"  - MAE: {lr_mae:.4f}")
print(f"  - MAPE: {lr_mape:.2f} %")
print(f"  - R2 Score: {lr_r2:.4f}")
print("-" * 30)
print(f"Decision Tree Regressor:")
print(f"  - MAE: {dt_mae:.4f}")
print(f"  - MAPE: {dt_mape:.2f} %")
print(f"  - R2 Score: {dt_r2:.4f}")
print("=" * 30)
