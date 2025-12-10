"""
Módulo: operacoes.py
Descrição: Edição, pesquisa e remoção de alunos usando DataFrame.
Autor: Arthur Torres e Maria Anna Pitzer
Data de criação: 04/12/2025

Funções principais: Exibir dados de operação, ler dados informados pelo ususário, pesquisar por alunos através do nome ou matrícula, editar informações existentes e remover registros do DataFrame.
"""

import pandas as pd 
from modules.arquivos import SaveDF
import os
import time

def Options(): #Funcao de opcoes 
    print("Insira a opção desejada: ") 
    print("[1] Inserir\n[2] Pesquisar\n[3] Sair\n")
    op = int(input("Opção: ")) 

    return op #Retorna a opcao digitada pelo user
    
def ReadInfo():
    data = {'Nome' : "", 'Rua' : "", 'Numero' : "", 'Bairro' : "",  
            'Cidade' : "", 'UF' : "", 'Telefone' : "", 'E-mail': ""} #dicionario de informacoes
    
    print("Insira os dados: ") 
    for info in data: #loop que insere os dados inseridos em cada chave do dicionario
        data[info] = input(f"{info}: ").strip()
    
    return data #retorna o dicionario

def Search(df): #função para pesquisar os dados
    termo = input("Digite o nome ou a matrícula do aluno: ") #pega o nome ou matricula

    resultado = df[df['Nome'].str.contains(termo, case=False) | (df['Matrícula'].astype(str) == termo)] #confere se a matricula existe

    if resultado.empty: #se não tiver avisa
        print("Nenhum aluno encontrado.") 
        return None #retorna vazio

    print("=====================================================================================================================")
    print("                                            RESULTADO DA PESQUISA                                                    ")
    ("=====================================================================================================================")
    print(resultado.to_string(index=False)) # mostra o resultado 

    
    confir = False #variavel booleana para edicao de dados
    if confirmation(confir): #Se o usuario quiser editar
        menu2(df, resultado) #Chama a funcao de opcoes exclusivas para edicao
    else:
        print("Voltando à página inicial...")

    return df #retorna para a função usar

#funcao com duas perguntas para duas verificações usadas no codigos
def confirmation(confir):
    pergunta = "\nDeseja editar os dados do aluno? (s/n): " 

    if confir: #Caso confir for true
        pergunta = "\nTem certeza que deseja remover este aluno(a)? (s/n): "

    while True: 
        op = input(pergunta).strip().lower() #Remove os espaços em branco e deixa em caixa baixa

        if op == 's': #
            return True
        if op == 'n':
            return False
        
        print("Valor inválido! Por favor, insira a resposta corretamente.")

#menu exclusivo da area de edição
def menu2(df, resultado): #Funcao de menu da area de pesquisa de dados
    while True: 
        print("\nSelecione uma das opções abaixo: ")
        print("[1] Editar\n[2] Remover\n[3] Voltar ao início\n")
        op = int(input("Opção: "))

        match op:
            case 1: #Se opcao for 1, edicao
                edit(df, resultado)
            case 2:
                remove(df, resultado) #Se for 2, remove
                break
            case 3: #Se for 3, retorna ao menu
                print("Retornando ao menu principal...")
                break
            case _: #Caso default para tratamento de erros
                print("Opção inválida! Escolha outra.")

#função de edicação de dados 
def edit(df, resultado):
    indice = resultado.index[0] #Pega o indice do resultado, ou seja, do aluno pesquisado
    print(f"Editando o aluno(a): {df.at[indice, 'Nome']}") 

    campos = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']

    while True: #mostra os campos possiveis de editar 
        print("\nEscolha o campo que deseja editar: ")
        for i, j in enumerate(campos, 1): #Loop que numera os campos de 1 a 9, sendo 0 a opção para sair
            print(f"{i} - {j} Atual: {df.at[indice, j]}") #Imprime no monitor as opções a serem escolhidas
        print("0 - Finalizar edição") 

        op = int(input("Opção: ")) 


        if op == 0: #Se a opcao for zero:
            SaveDF(df) #Salva o Df e volta para o menu anterior
            print("Salvando edição... Finalizando...")
            break

        if op == 1: #Se a opcao for 1:
            print("A matrícula do aluno não pode ser editada.") #A matricula n pode ser editada
            time.sleep(2) #Delay de 2 segundos 
            continue #Continua o loop

        #parte de seleção de valores de edição e edição em si
        if 1 <= op <= len(campos): # Enquanto opcao for maior que 1 e menor que o tamanho do array campos (9)
            campo = campos[op - 1] #campo recebe a info do array - 1 campo, pois o array começa en zero 
            novoValor = input(f"Digite um novo dado para {campo} Obs: se manter vazio não será alterado: ") #Usuario insere o novo dado

            if novoValor.strip() != "": #Caso o novo valor nao for vazio, retirando os espaços em branco
                df.at[indice, campo] = novoValor #Insere o novo valor no dataframe 
                print(f"{campo} atualizado!") 
            else:
                print("Valor mantido.")
        else:
            print("Opção inválida! informe outra.")

#função para a remoção de alunos tambem com confimação
def remove(df, resultado): 
    indice = resultado.index[0] #Pega o indice do resultado, ou seja, do aluno pesquisado
    confir = True #Confir fica true
    if confirmation(confir): #Passa confir(true) para a funcao de confirmação
        df.drop(indice, inplace=True) #Deleta a linha pelo index
        df.reset_index(drop=True, inplace=True) #Reorganiza o index do dataframe apos exclusao
        SaveDF(df) #Salva o DF
        print("Aluno removido com sucesso!")
        return True 
    else:
        print("Remoção cancelada.")
        return False

