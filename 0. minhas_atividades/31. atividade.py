import os
import time
os.system("clear")
soma = 0
contador = 0
while True:
    numero = float(input(f"Digite uma nota: "))
    
    if numero < 0:
        break

    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
else:
    print("Nenhum valor positivo foi inserido retardado: ")

print()
print("A media dos valores iseridos seu pau no cu e {media:.2f}")