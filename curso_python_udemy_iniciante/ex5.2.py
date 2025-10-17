# hora = int(input('digite um horario: '))

# if hora >= 0 and hora <= 11:
#  print(f'bom dia, horario: {hora}')
# elif hora >= 12 and hora <= 17:
#  print(f'boa tade, horario: {hora}')
# else:
#  print(f'boa noite, horario: {hora}')


""""
Versao abaixo a correção do professor
"""
entrada = input('digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'bom dia, horario: {hora}')
    elif hora >= 12 and hora <= 17:
        print(f'boa tade, horario: {hora}')
    elif hora >= 18 and hora <= 23:
        print(f'boa noite, horario: {hora}')
    else:
        print('Hora não reconhecida')

except:
    print('Por favor digite apenas numeros inteiros')