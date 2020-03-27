import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder


data = pd.read_csv("Data.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,3].values


#Categorical Data

labelx = LabelEncoder()
x[:,0]=labelx.fit_transform(x[:,0])
print(x)