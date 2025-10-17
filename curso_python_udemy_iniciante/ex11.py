def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

if multiplicacao % 2 == 0:
    print('seu número é par')
else:
    print('seu numero é impar')