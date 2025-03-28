import os

os.system("clear") # Limpa o Terminal.

# solicitando dados

nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))
nota_3 = float(input("Digite sua nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

# exibindo dados (saida)

print()
print(f"Final: {media}")


if media < 7:
    print("reprovado")

else:
    print("aprovado")