num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print('1-Adição')
print('2-Subtração')
print('3-Multiplicação')
print('4-Divisão')
operacao = int(input('Escolha uma das opções: '))

resultado = 0

if operacao == 1:
   resultado = num1 + num2

elif operacao == 2:
    resultado = num1 - num2

elif operacao == 3:
    resultado = num1 * num2

elif operacao == 4:
    resultado = num1 / num2

else:
    print('Numero digitado não compativel')

print(f'O resultado foi {resultado}')