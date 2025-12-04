from modules.operacoes import *

import pandas as pd
import os

def CreateDF(data):
    #Cria dataframe vazio
    ncolumns = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']
    df = pd.DataFrame(columns = ncolumns)

    #Preenche o dataframe com as informacoes do user
    df_info = pd.DataFrame(data, index = [(len(df) + 1)])
    df_info['Matrícula'] = AutoIncrementMatricula(df)
    df = pd.concat([df , df_info])

    print(df)
    SaveDF(df) #Chama a funcao para salvar

def SaveDF(df): #Salva o df em arquivo csv
    dir = './data'
    archive = 'info_alunos.csv'

    if not os.path.exists(dir):
        os.makedirs(dir)

    save = os.path.join(dir, archive)
    df.to_csv(save, index = False)