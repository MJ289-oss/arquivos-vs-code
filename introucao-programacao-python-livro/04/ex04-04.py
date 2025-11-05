salario = float(input('Quanto você ganha: '))

if salario > 1250:
    salario = salario * 1.1
    print(f'O aumento do seu salário foi {salario}')

if salario <= 1250:
    salario = salario * 1.15
    print(f'O aumento do seu salário foi {salario}')