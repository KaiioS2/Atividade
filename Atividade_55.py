import os
from dataclasses import dataclass

os.system("cls || clear") 

@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: int

lista_carros = []
QUANTIDADE_CLIENTES = 2

print("IKmforme os dados do cliente: ")
for i in range(QUANTIDADE_CLIENTES):
    carros = Carros(
        marca=input("Marca do veiculo: "),
        modelo=input("Modelo do veiculo: "),
        categoria=input("Categoria do veiculo: "),
        preco=input("Preço do veiuculo: ")
    )
    lista_carros.append(carros)

os.system("cls || clear")
print("\n== Exibindo dados do veiculo ==") 
for carros in lista_carros:
    print(f"Marca do veiculo: {carros.marca}")
    print(f"Modelo do veiculo: {carros.modelo}")
    print(f"Categoria do veiculo: {carros.categoria}")
    print(f"Preço do veiuculo: {carros.preco}")
    print()

print("= Salvando os dados dos carross =")
nome_arquivo = "dados_carros.txt"
with open(nome_arquivo, "w") as arquivo:
    for carros in lista_carros:
        arquivo.write(f"{carros.marca},{carros.modelo},{carros.categoria}, {carros.preco}\n")