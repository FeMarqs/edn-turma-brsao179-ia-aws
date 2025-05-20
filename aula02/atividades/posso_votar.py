from os import system
system('cls')

idade = int(input("Qual a sua idade? "))

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar!")