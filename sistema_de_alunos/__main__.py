"""
Módulo: __main__.py
Descrição: Arquivo de entrada da operação.
Autor: Arthur Torres e Maria Anna Pitzer
Data de criação: 04/12/2025

Funções principais: Saudar o ususário e inicializar o sistema mostrando ao usuário o primeiro menu de opções.
"""
from modules.operacoes import *
from modules.arquivos import *
import sys

def saudacao():
    print("===============================================================================================")
    print("                                     SISTEMA DE ALUNOS                                         ")
    print("===============================================================================================")
    print("\nSeja bem-vindo ao sistema de alunos!")

def menu(): #Funcao principal do sistema
    df = LoadDF() #Chama a funcao para carregar o Df para n ocorrer falhas
    while True: #Loop infinito até o usuario encerrar 
        op = Options() #Pega a opcao escolhida pelo usuario
        match op: #Determina o que ocorrera de acordo com a escolha
            case 1: #---- Inserir Dados ----
                data = ReadInfo() 
                df = AddDF(data)
            case 2: #---- Pesquisar Dados ----
                Search(df)
            case 3: #---- Encerrar Programa ----
                SaveDF(df)
                sys.exit(0)
            case _: #---- Caso a opcao escolhida esteja incorreta
                print("Opção inválida! Escolha outra.")

if __name__ == '__main__':
    saudacao()
    menu()
        