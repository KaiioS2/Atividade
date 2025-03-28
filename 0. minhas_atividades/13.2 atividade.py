import os

os.system("clear") # Limpa o Terminal.
print("""
===========calendario===========
1  \tDomigo
2  \tSegunda-Feira
3  \tTerça-Feira
4  \tQuarta-Feira
5  \tQuinta-Feira
6  \tSexta-Feira
7  \tSabado
""")
dia = int(input("Digite um Numero de 1 a 7: "))
match dia:
    case 1 | 7 :
       print("Final de semana")
    case 2 | 3 | 4 | 5 | 6 :
         resutado = print("Dia util")
    case _:
         resutado = print("Opçao invalida")



