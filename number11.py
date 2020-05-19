import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Original DataFrame: ")
print(diamonds.shape)
print("\n Duplicate rows of diamonds DataFrame")
print(diamonds.duplicated().sum())