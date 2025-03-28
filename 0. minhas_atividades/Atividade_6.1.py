import os

os.system("clear") # Limpa o Terminal.

# operaçoes logicas

print("Ola senhor ou senhora, pfv digite sua idade para votar")
print()
sua_idade = int(input("Digite sua idade: "))

if sua_idade < 18:
    print("nao pode votar")
elif sua_idade > 65:
    print("nao pode votar")
else:
    print("Bom voto")