# nome = input('digite seu nome: ')

# nome_1 = len(nome)

# if nome_1 <= 4:
#     print('Seu nome é curto')
# elif nome_1 <= 5 and nome_1 >= 6:
#     print('Seu nome é normal')
# else: 
#     print('Seu nome é muito grande')

"""
codigo acima apresenta erros
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Por favor, digite pelo menos uma letra')