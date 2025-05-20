import os
import time
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    data_nascimento: str
    funcao: str

def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        data_nascimento=input("Data de nascimento: "),
        funcao=input("Função: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")

def mostrar(Funcionario):
    if verificar_lista_vazia(Funcionario):
        return
    
    print("\n = Lista de nomes =")
    for funcionario in Funcionario:
        print(funcionario)

def atualizar(Funcionario):
    if verificar_lista_vazia(Funcionario):
        return

    print("\n = Lista de Fucionario =")
    for funcionario in Funcionario:
        print(funcionario)
    fucionario_antigo = input("Digite o nome do fucionario: ")
    if fucionario_antigo in Funcionario:
        novo_fucionario = input(f"Digite o novo nome para {fucionario_antigo}:"),
        cpf=input("CPF: "),
        data_nascimento=input("Data de nascimento: "),
        funcao=input("Função: ")
        indice = Funcionario.index(fucionario_antigo)
        Funcionario[indice] = novo_fucionario, cpf, data_nascimento, funcao

        print(f"Fucionario atualizado com sucesso !")
    else: 
        print(f"\nO fucionario não foi encontrado.")

def excluir(Funcionario):
    if verificar_lista_vazia(Funcionario):
        return      

    mostrar(Funcionario)

    nome_remover = input("Digite o nome que desja remover:")
    if nome_remover in  Funcionario:
        Funcionario.remove(nome_remover) 
        print(f"O nome {nome_remover} foi remmovido com sucesso ! ")
    else:
        print(f"\nO nome {nome_remover} não foi encontrado na lista>") 

lista_funcionarios = []

while True:
    print("= Gerenciador de nomes =")
    print("1 - Adicionar")
    print("2 - Listar nomes")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = int(input("Digite uma das opções:"))

    match opcao:
        case 1:
            adicionar(lista_funcionarios)
        case 2:
            mostrar(lista_funcionarios)
        case 3:
            atualizar(lista_funcionarios)
        case 4:
            excluir(lista_funcionarios)
        case 5:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 5:
        time.sleep(2)
    os.system("cls  || clear")