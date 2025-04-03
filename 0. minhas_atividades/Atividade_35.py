import os

os.system("clear") 

def tabuada(num):

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Add um numero: "))
tabuada(num)