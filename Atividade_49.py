import os
os.system("cls || clear")

lista_de_comida = []
lista_de_preco = []
resultado = 0
while True:
    print("""
\n========> Seja bem vindo ao Gourmet Tech <======== 
\n |     nome do prato      |     Preço 
\n |  Moqueca de ovos       | 25R$
\n |  Ovo pochê             | 30R$
\n |  Omelete recheado      | 40R$
\n |  Carbonara Tradicional | 35R$
\n |  Shakshuka             | 50R$
    """)
 
    opcao = input("\nEscolha um prato: ").lower()
    os.system("cls || clear")
    
    desejo = input("Deseja add mais um pedido ? ").lower()
    if desejo == "n":
        break 
    if opcao == "Moqueca de ovos":
        resultado += 25
    elif opcao == "Ovo pochê":
        resultado += 30
    elif opcao == "Omelete recheado":
        resultado += 40
    elif opcao == "Carbonara Tradicional":
        resultado += 35
    elif opcao == "Shakshuka":
        resultado += 50
    else:
        print("Prato n encontrado! ")
lista_de_comida.append(opcao)
lista_de_preco.append(resultado)

print("\n= Notinha =")
for i in enumerate(lista_de_comida, start=1):
        print(f"{i}:")
print(f"valor total {resultado}")