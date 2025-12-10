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


def AutoIncrementMatricula(df): #Funcao que auto incrementa a matricula do aluno
    base = 90401200 #Valor inicial da matricula
    if df.empty: #Se o dataframe estiver vazio, retornará o valor base como primeira matricula
        return base 

    if 'Matrícula' in df.columns and not df['Matrícula'].empty: #Se matricula estiver nas colunas e preenchida 
        max_matricula = df['Matrícula'].max() #Pega o maior valor da coluna
        return max_matricula + 1 #Retorna maior valor + 1
    else:
        return base 


def CreateDF():
    ncolumns = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail'] #Colunas do DF
    df = pd.DataFrame(columns = ncolumns) #Criação do DF
    SaveDF(df) #Funcao que salva o DF como arquivo csv
    
def AddDF(data): # Funcao que adiciona os dados ao df existente
    if CheckDF: #Caso o DF existir 
        df = ReadDF() #Le o DF ja existente
        df_info = pd.DataFrame([data]) #Pega as informacoes inseridas e coloca no df info
        df_info['Matrícula'] = AutoIncrementMatricula(df) #Chama a funcao de incrementar para calcular a matricula
        df = pd.concat([df, df_info], ignore_index=True) #Junta o df original com o de dados inseridos 
        SaveDF(df) #Salva o DF em csv
    else: #Caso nao exista o DF
        df = pd.DataFrame([data]) #Cria o Df ja com as informacoes inseridas
        df['Matrícula'] = AutoIncrementMatricula(df) #Pega o numero da matricula
        SaveDF(df) #Salva o DF
        
    return df #Retorna o DF preenchido

def ReadDF(): #Funcao de leitura do DF

    path = './data/info_alunos.csv' #Caminho em que o DF está localizado
    df = pd.read_csv(path) #Le o DF
    return df #Retorna o DF lido

def SaveDF(df): #Salva o df em arquivo csv
    dir = './data' #pasta do save
    archive = 'info_alunos.csv' #nome do arquivo

    if not os.path.exists(dir): #Caso a pasta nao exista
        os.makedirs(dir) #Cria a pasta

    save = os.path.join(dir, archive) #Variavel que armazena o endereço ja com o nome do arquivo
    df.to_csv(save, index = False) #Salva o DF

def CheckDF(): #Funcao que confere a existencia do DF na pasta data
    path = './data/info_alunos.csv' #caminho do arquivo

    if os.path.isfile(path): #Se o arquivo existir
        return True 
    else: 
        return False
    
def LoadDF(): #Funcao que Carrega o DF
    b = CheckDF() #Confere a existencia
    if b: #Se existir
        df = ReadDF() #Le o arquivo
    else:
        print("Arquivo não encontrado. Criando arquivo csv...") 
        CreateDF() #Cria o DF 
        df = ReadDF() #Le o DF 

    return df #Retorna o DF