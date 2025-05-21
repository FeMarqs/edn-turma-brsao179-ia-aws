from os import system
system('cls')

#Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão)
#entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. 
#Siga as especificações abaixo:
#A calculadora deve solicitar ao usuário que insira dois números e uma operação.​
#As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).​
#O programa deve continuar solicitando entradas até que uma operação válida seja concluída.​
#Trate os seguintes erros:​
#Entrada inválida (não numérica) para os números​
#Divisão por zero​
#Operação inválida​
#Use try/except para capturar e tratar os erros apropriadamente.​
#Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.​
#Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

def calculadora():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")

    while True:
        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")

    while True:
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Erro: operação inválida. Por favor, escolha entre +, -, * ou /.")
            continue

        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2

            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break  # Encerra o programa após operação bem-sucedida

        except ZeroDivisionError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

# Executa a calculadora
calculadora()
