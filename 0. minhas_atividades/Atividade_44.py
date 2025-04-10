import os
os.system("cls || clear")

soma = 0

def calcular(soma):
    return soma / 2

for i in range(2):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = calcular(soma)
if media >= 7:
    resultado = "vc esta Aprovado!"
else:
    resultado = "vc esta Reprovado!"

print(f"Sua media foi de {media:.1f}!")
print(f"{resultado}")