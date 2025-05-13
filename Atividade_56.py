import os
from dataclasses import dataclass

os.system("cls || clear") 

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: int

lista_livros = []
QUANTIDADE_LIVROS = 3

print("IKmforme os dados do cliente: ")
for i in range(QUANTIDADE_LIVROS):
    livros = Livros(
        nome=input("Marca do veiculo: "),
        autor=input("Modelo do veiculo: "),
        categoria=input("Categoria do veiculo: "),
        preco=input("Preço do veiuculo: ")
    )
    lista_livros.append(livros)

os.system("cls || clear")
print("\n== Exibindo dados do veiculo ==") 
for livros in lista_livros:
    print(f"Nome do livro: {livros.nome}")
    print(f"Modelo do veiculo: {livros.autor}")
    print(f"Categoria do veiculo: {livros.categoria}")
    print(f"Preço do veiuculo: {livros.preco}")
    print()

print("= Salvando os dados dos livros =")
nome_arquivo = "dados_livros.txt"
with open(nome_arquivo, "w") as arquivo:
    for carros in lista_livros:
        arquivo.write(f"{livros.nome},{livros.autor},{livros.categoria}, {livros.preco}\n")