num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

n = 1
resultado = 0

while n <= num1:
    resultado += num2
    n += 1    

print(f'{num1} x {num2} = {resultado}')