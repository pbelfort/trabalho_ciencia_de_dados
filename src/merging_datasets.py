import pandas as pd

def merge_datasets(firstDataFrame: pd.DataFrame,
                   secondDataframe: pd.DataFrame):
   
   # merging datasets
   merged_datasets = pd.merge(firstDataFrame,
             secondDataframe,
             how='inner',
             left_on='sigla_uf',
             right_on='sigla')
   
   dropedNaN = merged_datasets.dropna()
   
   # saved sanitized dataset
   dropedNaN.to_csv('../data/processed/dados_tratados.csv', 
                 sep=';', 
                 encoding='latin1'
                 )
   
   return dropedNaN