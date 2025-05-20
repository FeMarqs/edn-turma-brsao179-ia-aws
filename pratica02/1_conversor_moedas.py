from os import system
system('cls')

# 1 - Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

# Conversor de Moeda

# Valor em reais
valor_reais = 100.00

# Taxas de câmbio
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversões
valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

# Exibindo os resultados
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: US$ {valor_dolar:.2f}")
print(f"Valor em Euros: € {valor_euro:.2f}")
