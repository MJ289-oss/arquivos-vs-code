valor_final_produtos = 0
total_compras = 0

while True:
    codigo_compras = int(input('Digite o codigodo produto ou zero para sair: '))
    quantidade_produtos = int(input('Digite a quantidade de produtos: '))

    if codigo_compras == 0:
        print('Compras finalizadas')
        break

    elif codigo_compras == 1:
        preco_1 = 0.5
        valor_produto = preco_1 * quantidade_produtos
        valor_final_produtos += valor_produto
        total_compras += quantidade_produtos

    elif codigo_compras == 2:
        preco_2 = 1
        valor_produto = preco_2 * quantidade_produtos
        valor_final_produtos += valor_produto
        total_compras += quantidade_produtos

    elif codigo_compras == 3:
        preco_3 = 4
        valor_produto = preco_3 * quantidade_produtos
        valor_final_produtos += valor_produto
        total_compras += quantidade_produtos

    elif codigo_compras == 5:
        preco_4 = 7
        valor_produto = preco_4 * quantidade_produtos
        valor_final_produtos += valor_produto
        total_compras += quantidade_produtos

    elif codigo_compras == 9:
        preco_5 = 8
        valor_produto = preco_5 * quantidade_produtos
        valor_final_produtos += valor_produto
        total_compras += quantidade_produtos

    else:
        print('Código invalido')

print(f'O valor final dos produtos foi: R$ {valor_final_produtos}, e a quantidade de itens foi {total_compras}')