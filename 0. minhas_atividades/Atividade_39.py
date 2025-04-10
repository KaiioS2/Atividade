import os
os.system("cls || clear")

def media(n1, n2): 
    calcular = (n1 + n2) / 2
    return calcular

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

Mediana = media(n1,n2)

print()
print(f"Mediana: {Mediana}")