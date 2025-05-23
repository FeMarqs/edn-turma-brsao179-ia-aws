from os import system
system('cls')

#4- Verificador de Ano Bissexto
#Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
#Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else:
        print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")



#Teste com anos como 2000 (bissexto), 2100 (não bissexto), 2020 (bissexto) e 2023 (não bissexto).