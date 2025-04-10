import os
os.system("cls || clear")

def somar(n1, n2): 
    calcular = n1 + n2
    return calcular


def subtrair(n1, n2): 
    calcular = n1 - n2
    return calcular

def multiplicar(n1, n2): 
    calcular = n1 * n2
    return calcular

def dividir(n1, n2): 
    calcular = n1 / n2
    return calcular

def media(n1, n2): 
    calcular = n1 + n2 / 2
    return calcular

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = somar(n1,n2)
Subtraçao = subtrair(n1,n2)
Multiplicaçao = multiplicar(n1,n2)
Divisao = dividir(n1,n2)
Mediana = media(n1,n2)

print()
print(f"Soma: {soma}")
print(f"Subtraçao: {Subtraçao}")
print(f"Multiplicaçao: {Multiplicaçao}")
print(f"Divisao: {Divisao:.2f}")
print(f"Mediana: {Mediana}")