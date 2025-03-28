import os
import time
os.system("clear")

login = "Usuario"
senha = "190505"



for i in range(3):

    l = str(input("Digite seu login: "))
    s = str(input("Digite ssua senha: "))


    if senha == s and login == l:
         print("Seja bem vindo: ")
         break
    else:
         print("Acesso negado")
else:
    print("excesso de tentativas")