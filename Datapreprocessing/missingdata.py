# Importing the dataset
import csv
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Data.csv')
X = pd.DataFrame(dataset.iloc[:, :-1].values)
y = pd.DataFrame(dataset.iloc[:, 3].values)

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

