import os
import time
os.system("clear")

vlor_gorjeta = 0
preco_total = 0
while True:
    print("""
======================= MENU =======================
Codigo  \t\tprato   \t\tvalor                         
1  \tPicanha    \t25,00                               
2  \t\tLasanha  \t25,00                               
3  \t\tStrogonoff   \t\t18,00                         
4  \t\tBife acebolado   \t\t15,00                     
5  \t\tPao com ovo  \t\tDe graça bebe                 
====================================================  
    """)



    opcao = int(input(f"digite o prato(s) "))
    match opcao:
            case 1:
                prato = "Picanha"
                valor = 25
            case 2:
                prato = "Lasanha"
                valor = 25
            case 3:
                prato = "strogonoff"
                valor = 18
            case 4:
                prato = "Bife acebolado"
                valor = 15
            case 5:
                prato = "Pao com ovo"
                valor = 00
            case _:
                 resultado = "Opçao invalida" 
                
    preco_total += valor
    mais_pedidos = input("Mais pedidos? \nUse 'S' ou 'N' para responder: ").lower()

    if mais_pedidos == "n":
         break
if preco_total > 0:
     gorgeta_garcon = input("Deseja pagar 10% do valor da sua nota ao garcon? ").lower()
     if gorgeta_garcon == "s":
          valor_gojeta = preco_total * 0.10

total_a_pagar = preco_total + valor_gojeta

print("""\n===> Nota fiscal <===
""")
print(f"Valor da gorjeta R$ {valor_gojeta}")
print(f"Valor total da compra: R${total_a_pagar}")