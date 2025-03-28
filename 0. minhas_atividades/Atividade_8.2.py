import os

os.system("clear") # Limpa o Terminal.

nmr_1 = int(input("Digite o numero: "))
nmr_2 = int(input("Digite o numero: "))

if nmr_1 > nmr_2:
    maior = nmr_1
    menor = nmr_2
else:
    maior = nmr_2
    menor = nmr_1

print()
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")