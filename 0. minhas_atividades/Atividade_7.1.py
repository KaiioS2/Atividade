import os

os.system("clear") # Limpa o Terminal.

# operaçoes logicas

print("Ola senhor ou senhora, pfv digite sua idade para votar")
print()
sua_idade = int(input("Digite sua idade: "))

if sua_idade >= 18 and sua_idade <= 65:
     print("Voto obrigatorio")    
elif sua_idade <= 15:
     print ("nao pode votar")
elif sua_idade <= 16 or sua_idade <= 17:
    print("Voto opicional")       
else:
     print("Nao sao obrigado a votar")