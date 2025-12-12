valor_divida = int(input('Digite o valor da divida: '))
juros_mensal = float(input('Digite a porcentagem de juros: '))
valor_mensal_pago = int(input('Digite o valor mensal a ser pago: '))

juros_mensal = (juros_mensal / 100) + 1

divida = valor_divida * juros_mensal
meses = divida / valor_mensal_pago
juros_divida = divida - valor_divida

print(f'O numero de meses vai ser: {meses:.2f}, o total pago vai ser: R$ {divida:.2f}, e o total de juros vai ser: R$ {juros_divida:.2f}')