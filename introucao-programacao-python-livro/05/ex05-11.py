dep_inicial = int(input('digite o deposito inicial: '))
taxa_juros = float(input('digite a taxa de juros: '))
taxa_juros = taxa_juros / 100
mes = 1
ganho = 0

while mes <= 24:
    ganho = dep_inicial * taxa_juros
    dep_inicial = dep_inicial + ganho
    print(f'mes {mes} - saldo R$ {ganho:.2f}')
    mes += 1