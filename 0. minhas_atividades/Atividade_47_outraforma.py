import os
os.system("cls || clear")

lista_de_Numeros = []
QUANTIDADE = 5
maior_numero = 0
menor_numero = 0
def maiornumero(Numerogrande):
    maior_numero = max(lista_de_Numeros) 
    return maior_numero

def menornumero(Numeropequeno):
    menor_numero = min(lista_de_Numeros) 
    return menor_numero

for i in range(QUANTIDADE):
    Numeros = int(input(f"Digite o {i+1}° Numero(s): "))
    lista_de_Numeros.append(Numeros)
    os.system("cls || clear")

for i, item in enumerate(lista_de_Numeros, start= 1):
    print(f"numeros digitados: {item}")

Numerogrande = maiornumero(maior_numero)
Numeropequeno = menornumero(menor_numero)

print()
print(f"Maior numero Digitado: {Numerogrande}")
print(f"Menor numero Digitado: {Numeropequeno}")