import os

os.system("clear") # Limpa o Terminal.

dia = int(input("Digite sua nota: "))

import os

os.system("clear") # Limpa o Terminal.

match dia:
    case 1:
       resutado = print("Domingo")
       resutado = print("Final de semana")
    case 2:
         resutado = print("Segunda-Feira")
         resutado = print("Dia util")
    case 3:
         resutado = print("terça-feira")
         resutado = print("Dia util")
    case 4:    
         resutado = print("quarta-feira")
         resutado = print("Dia util")
    case 5:    
         resutado = print("quinta-feira")
         resutado = print("Dia util")
    case 6:    
         resutado = print("sexta-feira")
         resutado = print("Dia util")
    case 7:    
         resutado = print("sabado")
         resutado = print("Final de semana")
    case _:
         resutado = print("Opçao invalida")