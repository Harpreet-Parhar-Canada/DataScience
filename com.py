import csv
import pandas as pd
import matplotlib.pyplot as plt

# arrayForColumns = ['sector','group_category','community_name','count']
# data = pd.read_csv('https://data.calgary.ca/resource/848s-4m4z.csv');
# # deletingColumns =['geocoded_column','resident_count','count']

# # dataForEast = df[df['sector'] == 'EAST'].drop(deletingColumns,axis=1);
# # dataForNortheast = df[df['sector'] == 'NORTHEAST'];
# # dataForSouth = df[df['sector'] == 'SOUTH'];
# # dataForWest = df[df['sector'] == 'WEST'];

# filterData = pd.DataFrame(data,columns=arrayForColumns) 
# print(filterData)


data = pd.read_csv("Data.csv")
x=data.iloc[:,:-1].values
y=data.iloc[:,3].values
print(y)