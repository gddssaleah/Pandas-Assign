import pandas as pd

cars = pd.read_csv('cars.csv')

data = pd.concat([cars.head(),cars.tail()])

print(data)