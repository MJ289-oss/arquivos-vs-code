print('digite um numero abaixo para iniciar a conversao')
print('1 para dias')
print('2 para horas')
print('3 para minutos')
print('4 para sair')


while True:
    numero = int(input('digite um numero: '))

    if numero == 4:
        print('Progama finalizado')
        break

    elif numero == 1:
        valor = int(input('digite um numero para ser convertido de dias para segundo: '))
        resultado = valor * 86400
        print(f'a conversao de {valor} dias é: {resultado} segundos')
        
    elif numero == 2:
        valor = int(input('digite um numero para ser convertido de horas para segundo: '))
        resultado = valor * 3600
        print(f'a conversao de {valor} horas é: {resultado} segundos')
        
    elif numero == 3:
        valor = int(input('digite um numero para ser convertido de minutos para segundos: '))
        resultado = valor * 60
        print(f'a conversao de {valor} minutos é: {resultado} segundos')
       
    else:
        print(f"o valor {numero} não posssui registro no sistema")