import os
os.system("cls || clear")

soma = 0

def calcular(soma):
    return soma / 3

for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = calcular(soma)
print(f"Sua media foi de {media:.2f}!")