import os
from dataclasses import dataclass
os.system("cls || clear")


# criando uma classe.
@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Pessoa:
    # Variaves = Atributos
    nome: str
    Email: str
    endereco: Endereco
   # Funçao = Metodo
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"\nEmail: {self.Email}")
        print(f"\nendereco: {self.endereco.logradouro}, numero: {self.endereco.numero}, Cidade: {self.endereco.cidade}")


# Aplicando caracteristicas da classe
endereco1 = Endereco("Rua monteiro Lobato", 34, "Salvador")
pessoa1 = Pessoa("Kaio", "Kaiomae@gmail.com", endereco1)
pessoa1.exibir_dados()
