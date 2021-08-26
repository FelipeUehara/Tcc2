import pandas as pd
from datetime import datetime
from datetime import time
import os
import sys

filepath = os.path.dirname(os.path.abspath(__file__))
# Read file into a df
def read_day(day,tipo):
    day = str(day)
    filepaths = filepath+'/Backup/Dados/DadosATUALIZADOS/dados_rede/' 
    filename = day+'.csv'
    df = pd.read_csv(filepaths+filename)
    df = df[['horario',tipo]]
    return df

# create empty list with all minutes in a day
def reset():
    day_empty = {}
    hour = 0
    for hour in list(range(24)):
        for minute in list(range(60)):
            day_empty.update({time(hour,minute,0):0})
    return day_empty

# Create dictionary with the sum of all minutes
def sum_day(day,tipo):
    df = read_day(day,tipo)
    df['horario'] = df['horario'].apply(lambda x: datetime.strptime(x, '%H:%M:%S').time().replace(second = 0))
    day_empty = reset()
    keys = list(day_empty.keys())
    for key in keys:
        day_empty[key] = df[df['horario']==key][tipo].sum()
    day = day_empty
    return day

def transpose_file(filename):
    dftot = pd.read_csv(filename)
    dftot.T.to_csv(filename)
    return dftot.T

def main(maxdays):
    tipos = ['bytes','pacotes']
    for tipo in tipos:
        dftot = pd.DataFrame()
        for day in list(range(maxdays)):
            day = day + 1
            print("DIA:",day)
            df = sum_day(day,tipo)
            dftot = dftot.append(df,ignore_index = True)
            print("FIM:",day)
        dftot.to_csv(f'sharedData/dados_{tipo}.csv', header=True)
    return dftot