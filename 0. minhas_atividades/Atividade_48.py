import os
os.system("cls || clear")

lista_de_nnumero = []
QUANTIDADE = 6

def maior_menor(lista):
    menor = min(lista)
    maior = max(lista)
    return menor, maior

def solicitar_dados():
    ("= LISTA DE COMPRAS =")
    for i in range(QUANTIDADE):
        numero = int(input("Digite um numero para a lista: "))
        lista_de_nnumero.append(numero)
        os.system("cls || clear")

def mostrar_dados():
    print("\n= ITENS DA LISTA =")
    for i, numero in enumerate(lista_de_nnumero, start=1):
        print(f"{i}: {numero}")

    print(f"Maior numero: {maior}")
    print(f"Menor numero: {menor}")


solicitar_dados()
menor, maior = maior_menor(lista_de_nnumero)
mostrar_dados()