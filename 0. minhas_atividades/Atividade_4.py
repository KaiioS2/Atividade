import os

os.system("clear") # Limpa o Terminal.

# solicitando dados

numero_1 = float(input("Digite sua nota: "))
numero_2 = float(input("Digite sua nota: "))

soma = (numero_1 + numero_2)

media = (numero_1 + numero_2) / 2

produto = (numero_1 * numero_2)

print()
print(f"Media: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

if numero_1 < numero_2:
    print(F"Maior numero e:{numero_2}")

elif numero_2 < numero_1:
    print(f"Maior numero e: {numero_1}")

if numero_1 < numero_2:
    print(f"Menor Numero e: {numero_1}")

elif numero_2 < numero_1:
    print(f"Menor numero e: {numero_2}")

else:
    print("Sao iguais")