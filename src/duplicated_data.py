import pandas as pd

def count_duplicate(dataframe: pd.DataFrame):
   print(f'foram encontrados {dataframe.duplicated().sum()} dados duplicados')