import os
from dataclasses import dataclass

os.system("cls || clear") 

@dataclass
class Fucionario:
    nome: str
    data_de_admissao: int
    matricula: int
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: int
    endereco: str

lista_fucionario = []
lista_cliente = []
QUANTIDADE_PESSOAS = 3

print("IKmforme os dados do Fucionarios: ")
for i in range(QUANTIDADE_PESSOAS):
    fucionario = Fucionario(
        nome=input("Nome do Fucionario: "),
        data_de_admissao=input("Sua data de admiçao: "),
        matricula=input("Sua matricula: "),
        endereco=input("Seu enderesco: ")
    )
    lista_fucionario.append(fucionario)
    os.system("cls || clear") 

print("IKmforme os dados do cliente: ")
for i in range(QUANTIDADE_PESSOAS):
    cliente = Cliente(
        nome=input("Nome do Fucionario: "),
        data_de_nascimento=input("Sua data de Nascimento: "),
        endereco=input("Seu enderesco: ")
    )
    lista_cliente.append(cliente)
    os.system("cls || clear") 

os.system("cls || clear")
print("\n== Exibindo dados dos fucionarios ==") 
for fucionario in lista_fucionario:
    print(f"Nome do Fucionario: {fucionario.nome}")
    print(f"Data de Admissao: {fucionario.data_de_admissao}")
    print(f"MAtricula: {fucionario.matricula}")
    print(f"Endereço: {fucionario.endereco}")
    print()

os.system("cls || clear")
print("\n== Exibindo dados do cliente ==") 
for cliente in lista_cliente:
    print(f"nOME DO CLIENTE: {cliente.nome}")
    print(f"Data de nascimento: {cliente.data_de_nascimento}")
    print(f"Endereço: {cliente.endereco}")
    print()

print("= Salvando os dados dos fucionarios =")
nome_arquivo = "Dados_Fucionarios.txt"
with open(nome_arquivo, "w") as arquivo:
    for fucionario in lista_fucionario:
        arquivo.write(f"{fucionario.nome},{fucionario.data_de_admissao},{fucionario.matricula}, {fucionario.endereco}\n")

print("= Salvando os dados dos clientes =")
nome_arquivo = "Dados_CLientes.txt"
with open(nome_arquivo, "w") as arquivo:
    for cliente in lista_cliente:
        arquivo.write(f"{cliente.nome},{cliente.data_de_nascimento},{cliente.endereco}\n")