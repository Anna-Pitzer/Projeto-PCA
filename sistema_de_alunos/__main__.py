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
        op = Options(False)
        match op:
            case 1:
                data = ReadInfo(op)
                df = AddDF(data)
            case 2:
                aluno = Search(df)
                if aluno is not None:
                    op = Options(True)
                    if op == 1:
                        Edit(aluno)    
            case 3:
                SaveDF(df)
                sys.exit(0)
            case _:
                print("Opção inválida! Escolha outra")
    


if __name__ == '__main__':
    saudacao()
    menu()
        