import os
from datetime import datetime
os.system("cls || clear")

def ano(n1):  
    return datetime.now().year - n1


n1 = int(input("Digite o ano que vc nasceu: "))
ano_nascimento = ano(n1)

if n1 > 2025:
    print("esta errada")
elif n1 == 2025:
    print("Ce nem nasceu, rala daqui: ")
else:
    print()
    print(f"A sua idade e {ano_nascimento} ")