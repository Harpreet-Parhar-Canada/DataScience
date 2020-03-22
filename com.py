import csv
import pandas as pd

arrayForColumns = ['sector','group_category','community_name','count']
data = pd.read_csv('https://data.calgary.ca/resource/848s-4m4z.csv');
# deletingColumns =['geocoded_column','resident_count','count']

# dataForEast = df[df['sector'] == 'EAST'].drop(deletingColumns,axis=1);
# dataForNortheast = df[df['sector'] == 'NORTHEAST'];
# dataForSouth = df[df['sector'] == 'SOUTH'];
# dataForWest = df[df['sector'] == 'WEST'];

filterData = pd.DataFrame(data,columns=arrayForColumns) 
print(filterData)