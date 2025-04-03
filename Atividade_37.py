import os

os.system("clear") 



def parouimpa(num):
    if num > 0:
        print("Positivo: ")
    elif num == 0:
        print("Esse numero e neutro: ")
    else:
        print("Negativo: ")


   
num = int(input("Digite um numero: "))
parouimpa(num)