n = int(input('Tabuada de: '))
inicio = int(input('Digite de onde começa: '))
fim = int(input('Digite onde termina: '))


while inicio <= fim:
    print(f'{n} x {inicio} = {n * inicio}')
    inicio += 1