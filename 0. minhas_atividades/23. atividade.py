import os
import time
os.system("clear") # Limpa o Terminal.

media = 0
for i in range(4):
    numero = float(input("digite suas notas: "))
    media += numero / 4
print(f"Media: {media}")
