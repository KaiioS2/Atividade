import os
os.system("cls || clear")

notas = [] # Criando uma lista

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma / 3

print(f"Media {media}")

for nota in notas:
    print(f"NOta: {nota}")