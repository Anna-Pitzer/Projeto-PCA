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

def menu():
    df = LoadDF()
    while True:
        op = Options()
        match op:
            case 1:
                data = ReadInfo()
                df = AddDF(data)
            case 2:
                Search(df)
            case 3:
                SaveDF(df)
                sys.exit(0)
            case _:
                print("Opção inválida! Escolha outra")

if __name__ == '__main__':
    saudacao()
    menu()
        