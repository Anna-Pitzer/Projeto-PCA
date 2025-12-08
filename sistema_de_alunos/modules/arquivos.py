"""
Módulo: arquivos.py
Descrição: Gerencia um cadastro de alunos: criação, leitura, adição e armazenamento em CSV.
Autor: Arthur Torres e Maria Anna Pitzer
Data de criação: 04/12/2025

Funções principais: O módulo gerencia o arquivo de alunos. Ele possui uma função que calcula automaticamente a próxima matrícula disponível, outra que cria o arquivo CSV inicial, uma que adiciona novos alunos ao cadastro, outra que lê o CSV, outra que salva o DataFrame no arquivo, uma que verifica se o CSV existe e, por fim, uma função que carrega os dados existentes ou cria o arquivo caso ele ainda não exista.

Observações:
  O arquivo de dados é armazenado em './data/info_alunos.csv'. As colunas padrão são: Matrícula, Nome, Rua, Numero, Bairro, Cidade, UF, Telefone, E-mail e a matrícula inicial padrão: 90401200.
"""

from modules.operacoes import *
import pandas as pd
import os


def AutoIncrementMatricula(df):
    base = 90401200
    if df.empty:
        return base

    if 'Matrícula' in df.columns and not df['Matrícula'].empty:
        max_matricula = df['Matrícula'].max()
        return max_matricula + 1
    else:
        return base


def CreateDF():
    ncolumns = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']
    df = pd.DataFrame(columns = ncolumns)
    SaveDF(df)
    
def AddDF(data):
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
    
def LoadDF():
    b = CheckDF()
    if b:
        df = ReadDF()
    else:
        print("Arquivo não encontrado. Criando arquivo csv...")
        CreateDF()
        df = ReadDF()

    return df