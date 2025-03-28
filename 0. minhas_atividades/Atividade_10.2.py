import os

os.system("clear") # Limpa o Terminal.

maças = float(input("Digite seu numero: "))


if maças < 12:
    preco_maçan = 1.30
else:
    preco_maçan = 1.00

valor_total = maças * preco_maçan

print()
print(f"Valor total da compra RS {valor_total:.2f}")

