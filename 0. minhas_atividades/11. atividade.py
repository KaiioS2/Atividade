import os

os.system("clear") # Limpa o Terminal.

# solicitando dados

numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite um numero: "))

print()
operador = input("Digite o operador: ")

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2

print()
print(f"Primeiro Numero: {numero_1}")
print(f"Segundo Numero: {numero_2}")
print(f"Operador: {operador}")
print(f"resultado: {resultado}")