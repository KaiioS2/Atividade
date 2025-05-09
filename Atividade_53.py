import os
from dataclasses import dataclass

os.system("cls || clear") # Limpar terminal.

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = [] # Criando uma lista para adicionar clientes.
QUANTIDADE_CLIENTES = 2 # Costante que define  a quantidade de clientes.

# laço de repetiçao para adicionar clientes
print("IKmforme os dados do cliente: ")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome=input("Nome: "), # Nao esqueça da virgula.
        email=input("E-mail: "),
        telefone=input("telefone: ") # No ultimo nao tem virgula.
    )
    lista_clientes.append(cliente) # Adicionar um cliente na lista.

os.system("cls || clear") # Limpar terminal. 
# laço de repetiçao para exibir dados dos clientes
print("\n== Exibindo dados clientes ==") 
for cliente in lista_clientes: # Mostra os dados por elementos na lista.
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print()

# salvando em um arquivo .txt
print("= Salvando os dados dos clientes =")
nome_arquivo = "dados_clientes.txt"
# W -> Escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular
with open(nome_arquivo, "w") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome},{cliente.email},{cliente.telefone}\n")