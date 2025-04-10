import os
os.system("cls || clear")

def media(n1, n2, n3): 
    calcular = (n1 + n2 + n3) / 3
    return calcular

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

Mediana = media(n1,n2,n3)

print()
print(f"Mediana: {Mediana}")