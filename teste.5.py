import os
os.system("cls || clear")

# Criando uma lista
lista_de_compras = []
QUANTIDADE = 3

# Solicitando Dados para o usuario
print("= Lista de Compras =")
for i in range(QUANTIDADE):
    item = input(f"Digite o {i+1}° item para uma lista: ")
    lista_de_compras.append(item)

# Exibindo itens da lista de compras
print("\n= ITENS DA LISTA =")
for i, item in enumerate(lista_de_compras, start= 1):
    print(f"{i}° item: {item}")