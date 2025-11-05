inteiros = 0
numeros_digitados = 0
media = 0 

while True:
    valor = int(input('Digite um numero, caso seja 0 o programa finaliza: '))
    if valor == 0:
        break
    else:
        inteiros += valor
        numeros_digitados += 1

media = inteiros / numeros_digitados

print(f'A quantidade de numeros digitados foi: {numeros_digitados}, A soma dos numeros foi: {inteiros}, A media dos valores foi de: {media}')