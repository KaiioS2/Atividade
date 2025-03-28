import os

os.system("clear") # Limpa o Terminal.

valor = float(input("Digite um valor: "))

print("""
===========calendario===========
1  \tA vista
2  \tA prazo
""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

match forma_de_pagamento:
    case 1:
        desconto = valor * 0.10
        total = valor - desconto
        print()
        print(f"Valor: {valor}")
        print(f"Forma de pagamento: {forma_de_pagamento}")
        print(f"Valor do desconto: {desconto}")
        print(f"total: {total}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas: "))
        if parcelas >= 1 and parcelas <= 6:
            valor_parcelado = (valor / parcelas)

            print()
            print(f"Valor: {valor}")
            print(f"Parcelas: {parcelas}")
            print(f"Valor Parcelado: {valor_parcelado}")
            print(f"Forma de pagamento: {forma_de_pagamento}")
            print(f"Total: {valor}")
        else: 
            print("Aglguma coisa errada")
    case _:
            print("opçao invalida")