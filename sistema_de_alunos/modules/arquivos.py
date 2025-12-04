from modules.operacoes import *
import pandas as pd
import os

ncolumns = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']

def AutoIncrementMatricula(df):
    base = 90401200
    if df.empty:
        return base

    if 'Matrícula' in df.columns and not df['Matrícula'].empty:
        max_matricula = df['Matrícula'].max()
        return max_matricula + 1
    else:
        return base


def CreateDF(data):
    if CheckDF:
        df = ReadDF()
        df_info = pd.DataFrame([data])
        df_info['Matrícula'] = AutoIncrementMatricula(df)
        df = pd.concat([df, df_info], ignore_index=True)
        SaveDF(df)
    else: 
        df = pd.DataFrame([data])
        df['Matrícula'] = AutoIncrementMatricula(df)
        SaveDF(df)
        
    return df

def ReadDF():
    path = './data/info_alunos.csv'
    df = pd.read_csv(path)
    return df

def SaveDF(df): #Salva o df em arquivo csv
    dir = './data'
    archive = 'info_alunos.csv'

    if not os.path.exists(dir):
        os.makedirs(dir)

    save = os.path.join(dir, archive)
    df.to_csv(save, index = False)

def CheckDF():
    path = './data/info_alunos.csv'

    if os.path.isfile(path):
        return True
    else: 
        return False