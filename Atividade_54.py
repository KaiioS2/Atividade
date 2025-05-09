import os
from dataclasses import dataclass
os.system("cls || clear")


# criando uma classe.
@dataclass
class Autor:
    Nome: str
    Biografia: str

@dataclass
class Livro:
    # Variaves = Atributos
    Titulo: str
    Ano: int
    autor: Autor
   # Funçao = Metodo
    def exibir_dados(self):
        print(f"Titulo: {self.Titulo}")
        print(f"\nAno: {self.Ano}")
        print(f"\nNome do autor: {self.autor.Nome}, Biografia do autor : {self.autor.Biografia}")

autor1 = Autor("Kaiio", "Alem de muito lindo, e um belissimo autor. ")
livro1 = Livro("O ceu do amanhecer.", 2025, autor1)
livro1.exibir_dados()