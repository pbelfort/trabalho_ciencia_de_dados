import pandas as pd

def average_comparsion_region(dataframe:  pd.DataFrame):
    average_region = dataframe.groupby(['regiao','ano']).agg(
    media = ('consumo', 'mean')
    )    
    nordeste = average_region.query("regiao == 'Nordeste'")
    centro_oeste = average_region.query("regiao == 'Centro-Oeste'")
    comparsion = nordeste.merge(centro_oeste, on='ano', suffixes=('_nordeste', '_centro_oeste'))
    comparsion['year_grather_than'] = comparsion['media_nordeste'] >  comparsion['media_centro_oeste']
    print(comparsion)