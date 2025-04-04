import os
os.system("cls || clear")

def Metros(n1): 
    calculo = n1 * 10
    return calculo

def Metros2(n1):
    calculo = n1 * 10
    segundo_calculo = calculo * 10
    return segundo_calculo


n1 = int(input("Digite a quantidade de metros: "))

Metropolis = Metros(n1)
Metropolis2 = Metros2(n1)

print()
print(f"A quantidade de {n1} M, foi para {Metropolis} DM, que vira {Metropolis2} CM")