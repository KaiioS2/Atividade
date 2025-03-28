import os
import time
os.system("clear")

# Exemplo de uso do laço de repetiçao while.
while True:
    Nota = int(input("Digite sua nota: "))

    if Nota < 0 or Nota > 10:
        print("Nao autorizado. \nnota nao econtrada. \n")
    else:
        break

while True:
    Nota2 = int(input("Digite sua segunda nota: "))

    if Nota2 < 0 or Nota2 > 10:
        print("Nao autorizado. \nnota nao econtrada. \n")
    else:
        break

media = (Nota + Nota2) / 2

print()
print(f"Media: {media}")
print("Fim")