cigarros = int(input('quantos cigarros por dia você fuma: '))
anos = int(input('a quantos anos você fuma: '))

conversao_anos_dias = anos * 365
cigarros_quantidade = cigarros * conversao_anos_dias
tempo_vida_cigarro = cigarros_quantidade * 10
tempo_dia_cigarro = tempo_vida_cigarro / 1440

print(f'voce fumou: {cigarros_quantidade} cigarros em {conversao_anos_dias} dias e perdera {tempo_dia_cigarro:.0f} dias de vida')