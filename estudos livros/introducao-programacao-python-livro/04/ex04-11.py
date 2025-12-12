valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite qual o seu salario: '))
anos_pagar = int(input('Digite a quantidade de anos que voce vai pagar: '))

transform_ano_mes = anos_pagar * 12
prest_mensal = valor_casa / transform_ano_mes 
porcent_salario = salario * 0.3

if prest_mensal > porcent_salario:
    print('Seu imprestimo nao foi aprovado')

else:
    print('Seu imprestimo foi aprovado')