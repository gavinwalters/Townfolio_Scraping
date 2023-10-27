import os
import pandas as pd

directory = '/Users/gavin/Documents/Townfolio data'

for file in os.listdir(directory):
    if file.endswith('.xlsx'):
        print(file)
        filepath = directory + '/' + file
        print(pd.read_excel(filepath))