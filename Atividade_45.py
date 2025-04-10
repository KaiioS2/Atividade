import os
os.system("cls || clear")


def imc(peso, altura): 
    calcular = altura * altura
    resultado = peso / calcular
    return resultado
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = imc(peso, altura)

def Tabela():
    if IMC < 18.5:
        return "Abaixo do peso"
    elif IMC >= 18.5 and IMC <= 24.9:
        return "Peso normal"
    elif IMC >= 25 and IMC <= 29.9:
        return "Sobrepeso"
    elif IMC >= 30 and IMC <= 34.9:
        return "Obesidade grau 1"
    elif IMC >= 35 and IMC <= 29.9:
        return "Obesidade grau 2"
    elif IMC >= 40:
        return "Obesidade grau 3"

classificado = Tabela()

def Tabela2():
    if IMC < 18.5:
        return "COnsulte um nutricionista para orientaçao! "
    elif IMC >= 18.5 and IMC <= 24.9:
        return "Matenha Habitos saudaveis! "
    elif IMC >= 25 and IMC <= 29.9:
        return "Considere uma dieta balanceada e atividade fisica! "
    elif IMC >= 30 and IMC <= 34.9:
        return "Procure orientaçao de um proficional de saude! "
    elif IMC >= 35 and IMC <= 29.9:
        return "Consulte um medico para avaliaçao e orientaçao! "
    elif IMC >= 40:
        return "Busque assistencia medica imediatamente!!!"

Recomendacao = Tabela2()

print()
print(f"O seu peso {IMC:.1f}")
print()
print("classificaçao: ")
print(f"{classificado}")
print()
print("Recomendaçao: ")
print(f"{Recomendacao}")