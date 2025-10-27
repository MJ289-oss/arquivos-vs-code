consumo = int(input('Digite qual o seu consumo de energia por mes: '))
print('1 - residencial')
print('2 - industrial')
print('3 - comercial')
instalacao = int(input('Qual o tipo de instalacao: '))

total_pagar = 0

if instalacao == 1:
    if consumo > 500:
        total_pagar = consumo * 0.65
    else:
        total_pagar = consumo * 0.4

elif instalacao == 2:
    if consumo > 1000:
        total_pagar = consumo * 0.6
    else:
        total_pagar = consumo * 0.55

elif instalacao == 3:
    if consumo > 5000:
        total_pagar = consumo * 0.6
    else:
        total_pagar = consumo * 0.55

else:
    print('Nao identificado o numero inserido')

print(f'O valor final a ser pago sendo o consumo: {consumo} Kw\h, será de: R$ {total_pagar} ')
