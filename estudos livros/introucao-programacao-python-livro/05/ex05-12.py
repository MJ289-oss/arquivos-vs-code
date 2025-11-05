dep_inicial = int(input('digite o deposito inicial: '))
dep_mensal = int(input('digite o deposito mensal: '))
taxa_juros = float(input('digite a taxa de juros: '))
taxa_juros = (taxa_juros / 100) + 1
mes = 1
ganho = 0
resultado  = 0

while mes <= 24:
    if mes == 1:
        resultado = dep_inicial * taxa_juros
    else:
        resultado = (dep_mensal + resultado) * taxa_juros
    
    print(f'{resultado:.2f}')
    mes += 1   

