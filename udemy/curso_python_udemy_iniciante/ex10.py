cpf = '746.824.890-70' \
    .replace('-','') \
    .replace('.','')
nove_digitos = cpf[:9]
contador_regessivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regessivo_1
    contador_regessivo_1 -= 1
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regessivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regessivo_2
    contador_regessivo_2 -= 1
digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'{cpf} é valido')
else:
    print('cpf invalido')