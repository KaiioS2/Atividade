import os
os.system("cls || clear")

lista_de_Numeros = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    Numeros = int(input(f"Digite o {i+1}° Numero(s): "))
    lista_de_Numeros.append(Numeros)
    os.system("cls || clear")

maior_numero = max(lista_de_Numeros) 
menor_numero = min(lista_de_Numeros) 

print()
print(f"Maior numero Digitado: {maior_numero}")
print(f"Menor numero Digitado: {menor_numero}")

for i, item in enumerate(lista_de_Numeros, start= 1):
    print(f"numeros digitados: {item}")