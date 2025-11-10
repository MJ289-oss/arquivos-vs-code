ultimo1 = 0
ultimo2 = 0

fila1 = []
fila2 = []

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2")
    print(f"fila 1 atual: {fila1}, e fila 2 atual: {fila2}")
    print("digite F para fila 1 e G paraa filaa 2 adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento da fila 1 e B para a fila 2, S para sair.")
    operacao = str(input("Operação (F ou G, A ou B, ou S):")).upper()

    if "S" in operacao:
        print("Encerrando o programa...")
        break

    for indice in operacao:
        if indice == "A":
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)
                print(f"Cliente fila 1: {atendido1} atendido")
            else:
                print("Fila vazia! Ninguem para atender.")
        elif indice == "B":
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)
                print(f"Cliente fila 2: {atendido2} atendido")
            else:
                print("Fila vazia! Ninguem para atender.")
        elif indice == "F":
            ultimo1 += 1
            fila1.append(ultimo1)
        elif indice == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
        else:
            print("Operação invalida! Digite apenas F, A ou S!")