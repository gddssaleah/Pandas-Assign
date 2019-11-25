import pandas as pd

data = pd.read_csv('cars.csv')

a = data[1::2].head()

b = data.loc[data['Model']=='Mazda RX4']

c = data.loc[data['Model']=='Camaro Z28'].loc[:,['Model','cyl']]

d1 = data.loc[data['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic'])]
d = d1[['Model','cyl','gear']]

print(d)