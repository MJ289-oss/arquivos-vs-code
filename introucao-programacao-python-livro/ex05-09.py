num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

resultado = 0 
n = 0

while n <= num1:
    n += num2
    resultado += 1

print(f'{num1} / {num2} = {resultado - 1}')