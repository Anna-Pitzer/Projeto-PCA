from modules.operacoes import *
from modules.arquivos import *
import sys

def saudacao():
    print("===============================================================================================")
    print("                                     SISTEMA DE ALUNOS                                         ")
    print("===============================================================================================")
    print("\nSeja bem-vindo ao sistema de alunos!")

def menu():
    #df = carrega()
    
    while True:
        edit = False
        op = Options(edit)

        match op:
            case 1:
                data = ReadInfo(op)
                df = CreateDF(data)
            case 2:
                pesquisar(df)
            case 3:
                SaveDF(df)
                sys.exit(0)
            case _:
                print("Opção inválida! Escolha outra")
    


if __name__ == '__main__':
    saudacao()
    menu()
        