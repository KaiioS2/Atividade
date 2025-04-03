import os

os.system("clear") 



def parouimpa(num):
    if num % 2 == 0:
        print("Esse numero e par: ")
    else:
        print("Esse numero e impar: ")


   
num = int(input("Digite um numero: "))
parouimpa(num)