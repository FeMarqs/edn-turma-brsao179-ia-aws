from os import system
system('cls')

# 4 - Calculadora de Preço Total
# Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
# Preço do produto: R$ 12,40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

# Informações do produto
nome_produto = "Cadeira Infantil"
preco_produto = 12.40
quantidade = 3

# Cálculo do preço total
preco_total = preco_produto * quantidade

# Exibindo as informações
print("Produto:", nome_produto)
print("Preço unitário: R$", preco_produto)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)
