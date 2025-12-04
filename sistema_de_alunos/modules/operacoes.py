import pandas as pd 
from modules.arquivos import SaveDF
import os

def Options(edit):
    if (edit == False): 
        print("\nDigite a opçao desejada: ")
        op = int(input("[1] Inserir\n[2] Pesquisar\n[3] Sair\n"))
        return op
    # else: - comentei isso aq pq eu nn usei se tu for usar tu descomenta
    #     print("Digite qual dado deseja editar: ")
    #     op = int (input("[1] Nome\n[2] Endereço\n[3] Telefone\n[4] E-mail\n"))   
    #     return op + 3 

#depois tu faz essa função pra carregar o data frame que ja existe quando inicia o programa pq pelo oq eu entendi nn tinha
# def carrega():
    
def ReadInfo(op): #Le os dados de acordo com a opcao escolhida pelo user
    match (op):
        case 1: # Case 1: Le todas as informacoes do aluno e armazena em um dicionario para depois coloca-lo no dataframe
            print("Insira os dados: ")
            nome = input("Nome: ")
            rua = input("Rua: ")
            n = int(input("Número: "))
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            uf = input("UF: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            
            data = {'Nome' : nome, 'Rua' : rua, 'Numero' : n, 'Bairro' : bairro, 
                    'Cidade' : cidade, 'UF' : uf, 'Telefone' : telefone, 'E-mail': email}
            return data
        
        case _: #Case default caso a opcao seja invalida
            print("Opção Inválida. Tente novamente")
            Options()

def pesquisar(df): #função para pesquisar os dados
    termo = input("Digite o nome ou a matrícula do aluno: ") #pega o nome ou matricula

    resultado = df[df['Nome'].str.contains(termo, case=False) | (df['Matrícula'].astype(str) == termo)] #ve se tem la

    if resultado.empty: #se não tiver avisa
        print("Nenhum aluno encontrado.")
        return
    
    #coloquei isso mas acho que não está funcionando
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    print("=====================================================================================================================")
    ("                                            RESULTADO DA PESQUISA                                                    ")
    ("=====================================================================================================================")
    print(resultado.to_string(index=False)) # mostra o resultado 
    return menu(df, resultado) #retorna para a função usar

def menu(df, resultado):
    while True: #escolha uma opção
        print("\nSelecione uma das opções abaixo: ")
        print("1 - EDITAR")
        print("2 - REMOVER")
        print("3 - VOLTAR AO INICIO")

        op = int(input("Opção: "))

        match op:
            #case 1: 
                #df = editar(df, resultado)
            #case 2:
                #df = remover(df, resultado)
            case 3:
                print("Retornando ao menu principal...")
                break
            case _:
                print("Opção inválida! Escolha outra.")