import os
os.system("cls || clear")
contador = 0
soma = 0

def media(n1, soma, contador): 
        calcular = (n1 + soma)
        meidar = calcular / contador
        return meidar

while True:

    n1 = int(input("Digite o primeiro numero: "))
    soma += n1
    contador += 1
    
    desejo = input("Deseja add mais um numero ? ").upper()

    if desejo == "N":
        break

Mediana = media(n1, soma, contador) 

print()
print(f"Media: {Mediana}")