import os
import time
os.system("clear")
quantidade = 3
soma = 0 
for i in range(quantidade):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota invalida, tente novamente.")
        else:
            soma += nota
            break

media = soma / quantidade
print()
print(f"Media: {media:.1f}")
print()
if media >= 7:
    print("APROVADO: ")
elif media >= 5 and media < 7: 
    print("Recuperaçao")
else:
    print("Reprovado")
print()