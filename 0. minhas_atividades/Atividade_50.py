import os
from dataclasses import dataclass
os.system("cls || clear")


# criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    # Aplicando caracteristicas.
Pessoa1 = Pessoa(
    nome = input("Digite o nome: "),
    idade = int(input("Digite a idade: ")),
    peso = float(input("Digite o peso: ")),
    altura = float(input("Digite o Altura: "))
    )

os.system("cls || clear")


Pessoa2 = Pessoa(
    nome = input("Digite o nome: "),
    idade = int(input("Digite o idade: ")),
    peso = float(input("Digite o peso: ")),
    altura = float(input("Digite o Altura: "))
    )

print('\n= Dados da pessoa =')
print(f"\nNome: {Pessoa1.nome}, idade: {Pessoa1.idade} Anos, peso: {Pessoa1.peso} Kg, Altura: {Pessoa1.altura} M")
print(f"\nNome: {Pessoa2.nome}, idade: {Pessoa2.idade} Anos, peso: {Pessoa2.peso} Kg, Altura: {Pessoa2.altura} M")
