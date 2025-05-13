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
        nome=input("Nome do livro: "),
        autor=input("Autor do Livro: "),
        categoria=input("Categoria do Livro: "),
        preco=input("Preço do Livro: ")
    )
    lista_livros.append(livros)

os.system("cls || clear")
print("\n== Exibindo dados do veiculo ==") 
for livros in lista_livros:
    print(f"Nome do livro: {livros.nome}")
    print(f"Autor do livro: {livros.autor}")
    print(f"Categoria do livro: {livros.categoria}")
    print(f"Preço do livro: {livros.preco}")
    print()

print("= Salvando os dados dos livros =")
nome_arquivo = "dados_livros.txt"
with open(nome_arquivo, "w") as arquivo:
    for livros in lista_livros:
        arquivo.write(f"{livros.nome},{livros.autor},{livros.categoria}, {livros.preco}\n")