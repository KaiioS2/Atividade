import os
os.system("cls || clear")

contador = 0
soma = 0

# Função para calcular a média
def media(soma, contador): 
    if contador > 0:
        return soma / contador
    else:
        return 0

while True:
    n1 = int(input("Digite o número: "))  # Aqui você pode pedir qualquer número
    soma += n1  # Acumula a soma dos números
    contador += 1  # Incrementa o contador

    desejo = input("Deseja adicionar mais um número? (S/N): ").upper()
    if desejo == "N":
        break

# Calcula a média com a soma acumulada e o número de elementos
mediana = media(soma, contador)

# Exibe a média
print()
print(f"Média: {mediana}")