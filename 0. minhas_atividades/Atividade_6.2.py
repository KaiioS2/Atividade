import os

os.system("clear") # Limpa o Terminal.

# operaçoes logicas

print("Ola senhor ou senhora, pfv digite sua idade para votar")
print()
sua_idade = int(input("Digite sua idade: "))

if sua_idade < 18 or sua_idade > 65:
     print("Nao e obrigado a votar")
else:
     print ("e obrigado a votar")