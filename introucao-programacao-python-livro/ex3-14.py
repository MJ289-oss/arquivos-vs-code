distancia_percorrida = float(input('qual foi a distancia percorrida: '))
dias_alugados = int(input('quantos dias o carro foi alugado: '))

preco_dia = 60 * dias_alugados
preco_distancia = 0.15 * distancia_percorrida
preco_final = preco_dia + preco_distancia

print(f"o total a pagar é de R$ {preco_final}")
