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
if dia > 1 and dia < 7:
    resultado = "dia util."
elif dia == 1 or dia == 7:
    resultado = "Fim de semana"
else:
    resultado = "opçao invalida"
print()
print(f"Resultado: {resultado}")