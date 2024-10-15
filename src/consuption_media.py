import pandas as pd

def consuption_media(dataframe: pd.DataFrame):
    filter = (dataframe['sigla_uf'] == 'MG') & (dataframe['tipo_consumo'] == 'Residencial')
    data = dataframe[filter]
    consupution_media = data['consumo'].mean()
    print(f"Media de consumo: {consupution_media:.2f}")