import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(diamonds.head())
print("Numbers of rows and columns :")
print(diamonds.shape)
print("After dropping those rows whose where values are missing : ")
print(diamonds.dopna(how='any').shape)