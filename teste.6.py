import os
os.system("cls || clear")

from dataclasses import dataclass

# criando uma classe.
@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Aplicando caracteristicas.
Pessoa1 = Pessoa("Ana", 18)
Pessoa2 = Pessoa("Kaiio", 20)

# Aplicando caracteristicas do pet.

pet1 = Pet("Kayke", 4 , 7.8)
pet2 = Pet("Felipe", 2 , 9.8)


print('\n= Dados da pessoa =')
print(f"\nNome: {Pessoa1.nome} tem {Pessoa1.idade} anos")
print(f"\nNome: {Pessoa2.nome} tem {Pessoa2.idade} anos")

print('\n= Dados do pet =')
print(f"\nNome: {pet1.nome}, idade: {pet1.idade}, peso {pet1.peso} KG")
print(f"\nNome: {pet2.nome}, idade: {pet2.idade}, peso {pet2.peso} KG")