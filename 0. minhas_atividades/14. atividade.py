import os

os.system("clear") # Limpa o Terminal.

mes = int(input("Digite um numero: "))

import os

os.system("clear") # Limpa o Terminal.

match mes:
    case 1:
       resutado = print("Janeiro")
    case 2:
         resutado = print("Fevereiro")
    case 3:
         resutado = print("Março")
    case 4:    
         resutado = print("Abril")
    case 5:    
         resutado = print("Maio")
    case 6:    
         resutado = print("Junho")
    case 7:    
         resutado = print("julho")
    case 1:
       resutado = print("Agosto")
    case 2:
         resutado = print("Setembro")
    case 3:
         resutado = print("Outubro")
    case 4:    
         resutado = print("Novembro")
    case 5:    
         resutado = print("Desembro")
    case _:
         resutado = print("Opçao invalida")