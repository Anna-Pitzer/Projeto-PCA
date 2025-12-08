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

def Options():
    print("Insira a opção desejada: ")
    print("[1] Inserir\n[2] Pesquisar\n[3] Sair\n")
    op = int(input("Opção: "))

    return op
    
def ReadInfo():
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

def Search(df): #função para pesquisar os dados
    termo = input("Digite o nome ou a matrícula do aluno: ") #pega o nome ou matricula

    resultado = df[df['Nome'].str.contains(termo, case=False) | (df['Matrícula'].astype(str) == termo)] #ve se tem la

    if resultado.empty: #se não tiver avisa
        print("Nenhum aluno encontrado.")
        return None
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    print("=====================================================================================================================")
    print("                                            RESULTADO DA PESQUISA                                                    ")
    ("=====================================================================================================================")
    print(resultado.to_string(index=False)) # mostra o resultado 

    #pergunta se o usuario quer editar os dados (troquei o lugar pra ca pq nn considerei que era certo essa verificação ficar la na main)
    confir = False
    if confirmation(confir):
        menu2(df, resultado)
    else:
        print("Voltando à página inicial...")

    return df #retorna para a função usar

#funcao com duas perguntas para duas verificações usadas no codigos
def confirmation(confir):
    pergunta = "\nDeseja editar os dados do aluno? (s/n): "

    if confir:
        pergunta = "\nTem certeza que deseja remover este aluno(a)? (s/n): "

    while True:
        op = input(pergunta).strip().lower()

        if op == 's':
            return True
        if op == 'n':
            return False
        
        print("Valor inválido! Por favor informe outro.")

#menu exclusivo da area de edição
def menu2(df, resultado):
    while True: 
        print("\nSelecione uma das opções abaixo: ")
        print("[1] Editar\n[2] Remover\n[3] Voltar ao início\n")
        op = int(input("Opção: "))

        match op:
            case 1:
                edit(df, resultado)
            case 2:
                remove(df, resultado)
                break
            case 3:
                print("Retornando ao menu principal...")
                break
            case _:
                print("Opção inválida! Escolha outra.")

#função de edicação de dados
def edit(df, resultado):
    indice = resultado.index[0]
    print(f"Editando o aluno(a) {df.at[indice, 'Nome']}")

    campos = ['Matrícula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'E-mail']

    while True: #mostra os campos possiveis de editar 
        print("\nEscolha o campo que deseja editar: ")
        for i, j in enumerate(campos, 1):
            print(f"{i} - {j} Atual: {df.at[indice, j]}")
        print("0 - Finalizar edição")

        op = int(input("Opção: "))

        if op == 0:
            SaveDF(df)
            print("Salvando edição... Finalizando...")
            break

        #parte de seleção de valores de edição e edição em si
        if 1 <= op <= len(campos):
            campo = campos[op - 1]
            novoValor = input(f"Digite um novo dado para {campo} Obs: se manter vazio não será alterado: ")

            if novoValor.strip() != "":
                df.at[indice, campo] = novoValor
                print(f"{campo} atualizado!")
            else:
                print("Valor mantido.")
        else:
            print("Opção inválida! informe outra.")

#função para a remoção de alunos tambem com confimação
def remove(df, resultado):
    indice = resultado.index[0]
    confir = True
    if confirmation(confir):
        df.drop(indice, inplace=True)
        df.reset_index(drop=True, inplace=True)
        SaveDF(df)
        print("Aluno removido com sucesso!")
        return True
    else:
        print("Remoção cancelada.")
        return False

