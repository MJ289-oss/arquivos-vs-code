lista1 = [1, 2, 3, 4]
lista2 = [5, 4, 2, 6]

lista3 = []

for elemento in lista1:
    lista3.append(elemento)

for elemento in lista2:
    if elemento not in lista3:
        lista3.append(elemento)

print(lista3)