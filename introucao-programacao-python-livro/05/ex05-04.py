fim = int(input('Digite o ultimo número a imprimir: '))

x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1