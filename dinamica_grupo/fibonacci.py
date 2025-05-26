# Faça um programa que peça um número n e mostre os n primeiros números da sequência de Fibonacci.

def fibonacci(n):

    sequencia = []
    num1, num2 = 0, 1

    for _ in range(n):
        sequencia.append(num1)
        num1, num2 = num2, num1 + num2  

    return sequencia

num_seq = int(input("Informe a quatidade de números da sequência de Fibonacci: "))

result = fibonacci(num_seq)

print(f"Sequência Fibonacci: {result}")