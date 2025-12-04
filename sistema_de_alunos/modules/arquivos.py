from modules.operacoes import *
import pandas as pd
import os

caminhoArq = './data'
arq = 'info_alunos.csv'
ncolumns = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']

#passei pra ca pq ela nn funcionava de jeito nenhum la
def AutoIncrementMatricula(df):
    base = 90401201
    if df.empty:
        return base

    if 'Matrícula' in df.columns and not df['Matrícula'].empty:
        max_matricula = df['Matrícula'].max()
        return max_matricula + 1
    else:
        return base


def CreateDF(data):
    #df = carrega()  
    df_info = pd.DataFrame([data])
    df_info['Matrícula'] = AutoIncrementMatricula(df)
    df = pd.concat([df, df_info], ignore_index=True)

    print(df)
    SaveDF(df)
    return df

def SaveDF(df): #Salva o df em arquivo csv
    dir = './data'
    archive = 'info_alunos.csv'

    if not os.path.exists(dir):
        os.makedirs(dir)

    save = os.path.join(dir, archive)
    df.to_csv(save, index = False)