import os
os.system("cls || clear")

def valor(n1): 
    if n1 < 100:
        resultado = n1 *  1.10
        return resultado   
    else:
        resultado = n1 * 1.20
        return resultado

n1 = float(input("Digite o valor da compra: "))

Imposto = valor(n1)

print()
print(f"A compra saiu por R$ {Imposto:.2f}: ")
