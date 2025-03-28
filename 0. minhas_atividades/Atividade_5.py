import os

os.system("clear") # Limpa o Terminal.

# solicitando dados
login = str(input("Digite seu email: "))
senha_2 = int(input("Digite sua senha: "))

login = "kaio"
senha = 1221

if login == login and senha == senha_2:
    print("Bem vindo")
else:
    print("login invalido")