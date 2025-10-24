valor_produto = float(input('digite o valor do produto: '))
desconto = int(input('digite o percentual do desconto: '))
desconto = desconto / 100

valor_final = valor_produto - (valor_produto * desconto)
valor_desconto = (valor_produto * desconto)

print(f"O valor do produto é R$ {valor_produto}, o desconto foi de R$ {valor_desconto}, tendo o valor final do produto R$ {valor_final}")