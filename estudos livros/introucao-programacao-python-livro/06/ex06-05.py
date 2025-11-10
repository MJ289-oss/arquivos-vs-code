ultimo = 0
fila = []

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite:")
    print("F para adicionar um cliente ao fim da fila")
    print("A para atender um cliente")
    print("S para sair")
    operacao = input("Operações (ex: FFAAAS): ").upper()

    if "S" in operacao:
        print("Encerrando o programa...")
        break

    for indice in operacao:
        if indice == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif indice == "F":
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} adicionado ao fim da fila.")
        else:
            print(f"Operação inválida: {indice}")