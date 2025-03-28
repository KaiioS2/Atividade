

#Maior e menor numero

numero_1 = int(input("Digite sua nota: "))
numero_2 = int(input("Digite sua nota: "))

import os

os.system("clear") # Limpa o Terminal.

print(f"Numero 1: {numero_1}")
print(f"Numero 2: {numero_2}")

if numero_1 < numero_2:
    print(f"Maior numero e:{numero_2}")

elif numero_2 < numero_1:
    print(f"Maior numero e: {numero_1}")

if numero_1 < numero_2:
    print(f"Menor Numero e: {numero_1}")

elif numero_2 < numero_1:
    print(f"Menor numero e: {numero_2}")

else:
    print("Sao iguais")