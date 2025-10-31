salario = int(input('digite seu salario: '))
aumento = float(input("digite em quantos por cento seu salario aumentou: "))
aumento = (aumento / 100) + 1

valor_aumento = (salario * aumento) - salario
valor_final = salario + valor_aumento

print(f"seu  aumento foi R$ {valor_aumento:.2f} e o salario final foi R$ {valor_final:.2f}")