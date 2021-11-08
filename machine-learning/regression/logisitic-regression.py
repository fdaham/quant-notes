import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Extract dependent and predictor vars
df = pd.read_csv('../50_Startups.csv')
df = df.dropna()
x = df.drop('State', axis = 1)
# Convert dependent var to binary categories
y = df['State'] = (df['State'] == 'New York').astype(int)

# Get predicted model parameters
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
model = LogisticRegression(random_state=0)
model.fit(x_train, y_train)

# Check model accuracy
p_pred = model.predict_proba(x_test)
y_pred = model.predict(x_test)
r2 = model.score(x_test, y_test)
conf_m = confusion_matrix(y_test, y_pred)
