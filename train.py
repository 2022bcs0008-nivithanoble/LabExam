import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib
import json
import os

df = pd.read_csv('dataset/winequality-red.csv')
X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

os.makedirs('output/models', exist_ok=True)
os.makedirs('output/metrics', exist_ok=True)

joblib.dump(model, 'output/models/model.pkl')
with open('output/metrics/metrics.json', 'w') as f:
    json.dump({'mse': mse, 'r2': r2}, f)

print(f'Mean Squared Error: {mse}')
print(f'R2 Score: {r2}')