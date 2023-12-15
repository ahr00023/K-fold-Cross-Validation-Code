import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.datasets import load_wine
from sklearn.metrics import f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
import time

# Load the Wine dataset from UCI
wine = load_wine()
X = wine.data
y = wine.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an MLP classifier
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=5000)

# Define the number of folds for cross-validation
k = 10

# Perform k-fold cross-validation on the training data
kf = KFold(n_splits=k, shuffle=True, random_state=42)
start_train_time = time.time()
scores = cross_val_score(model, X_train, y_train, cv=kf)
end_train_time = time.time()


train_time = end_train_time - start_train_time

# Fit the MLP model on the entire training data
start_test_time = time.time()
model.fit(X_train, y_train)
end_test_time = time.time()

# Predict the labels for the test data
y_pred = model.predict(X_test)

# Calculate the testing time
test_time = end_test_time - start_test_time

# Print the classification report
print(classification_report(y_test, y_pred, target_names=wine.target_names))
print(f"Training Time: {train_time:.4f} seconds")
print(f"Testing Time: {test_time:.4f} seconds")

# Calculate the F1-score
f1 = f1_score(y_test, y_pred, average='weighted')

# Print the F1-score
print(f"F1-Score: {f1}")
