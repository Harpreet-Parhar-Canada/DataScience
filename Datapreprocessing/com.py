import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

data = pd.read_csv("Data.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,3].values


# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

#Categorical Data

labelx = LabelEncoder()
x[:,0]=labelx.fit_transform(x[:,0])

print(x)