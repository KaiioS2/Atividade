import os
import time
os.system("clear")

login = "Usuario"
senha = "190505"

while True:
    l = input("Digite seu login: ")
    s = input("Digite ssua senha: ")


    if senha == s and login == l:
        print("Seja bem vindo: ")
        break
    else:
        print("Acesso negado: ")
