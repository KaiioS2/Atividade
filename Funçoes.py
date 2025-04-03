import os

os.system("clear") 

#funçao sem retorno.
#Definindo Caracteristicas da funçao.
def saudacao(nome):
    print(f"Ola {nome}! Bem vindo ao curso de DS! ")

nome_visitante = input("Digite seu nome: ")
saudacao(nome_visitante) # chamando a funçao.

# Crie uma funçao com o nome: diciplina que receba 
# o nome de diciplinma do curso de Ds.
# Mostre o texto: a diciplina **** faz parte do curso de DS.

def diciplina(materia):
    print(f"Ola! seja bem vindo ao curso de {materia} ")

materia = input("Digite seu curso: ")
diciplina(materia)