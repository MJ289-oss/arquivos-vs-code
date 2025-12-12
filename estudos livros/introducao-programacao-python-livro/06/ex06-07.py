def verifica_parenteses(expressao):
    pilha = []
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return "Erro"
            pilha.pop()
    
    if not pilha:
        return "Ok"
    else:
        return "erro"
    
print(verifica_parenteses('(())'))