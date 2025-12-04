import pandas as pd 
import os

def Options(edit):
    if (edit == False): 
        print("Digite a opçao desejada: ")
        op = int (input("[1] Inserir\n[2] Pesquisar\n[3] Sair\n"))
        return op
    else: 
        print("Digite qual dado deseja editar: ")
        op = int (input("[1] Nome\n[2] Endereço\n[3] Telefone\n[4] E-mail\n"))   
        return op + 3 



def AutoIncrementMatricula(df): #Essa funcao faz a configuração automatica da matricula, 
    rows = len(df)
    if rows == 1: return 1
    increment = 90401200 + (rows + 1)
    return increment
    
def ReadInfo(op): #Le os dados de acordo com a opcao escolhida pelo user
    match (op):
        case 1: # Case 1: Le todas as informacoes do aluno e armazena em um dicionario para depois coloca-lo no dataframe
            data = {'Nome' : "", 'Rua' : "", 'Numero' : "", 'Bairro' : "", 
                    'Cidade' : "", 'UF' : "", 'Telefone' : "", 'E-mail': ""}
            
            print("Insira os dados: ")
            data['Nome'] = input("Nome: ")
            data['Rua'] = input("Rua: ")
            data['Numero'] = int (input("Número: "))
            data['Bairro'] = input("Bairro: ")
            data['Cidade'] = input("Cidade: ")
            data['UF'] = input("UF: ")
            data['Telefone'] = input("Telefone: ")
            data['E-mail'] = input("E-mail: ")
            
            return data
        
        case _: #Case default caso a opcao seja invalida
            print("Opção Inválida. Tente novamente")
            Options()


