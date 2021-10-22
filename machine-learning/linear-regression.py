import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Extract dependent var and predictor vars
df = pd.read_csv('50_Startups.csv')
df = df.dropna()
x = df.drop('Profit', axis = 1)
y = df[['Profit']]

# Handle categorical vars by turning them into dummy indicator vars
x = pd.get_dummies(x, drop_first = True)

# Get predicted model parameters
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
model = LinearRegression().fit(x_train, y_train)
y_pred = model.predict(x_test)

# Check model accuracy
r2 = model.score(x_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print('R-Squared Error = ', r2)
print('Mean Squared Error = ', mse)
