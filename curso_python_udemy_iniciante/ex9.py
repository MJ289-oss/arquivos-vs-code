import os
lista_compra = []
valor = 0

while True:
     print('lista de compras:')
     print('1 para sair')
     print('2 para inserir')
     print('3 para excluir')
     print('4 para ver os itens')
     valor = int(input('digite um dos valores desejados acima: '))
    
     if valor == 2:
         os.system('cls')
         item = input(f'\nadicione um produto na lista de compras: ')
         lista_compra.append(item)

     elif valor == 3:
         del lista_compra[-1]

     elif valor == 4:
         os.system('cls')
         if len(lista_compra) == 0:
             print(f'\nNão há nenhum produto')

         else:
          for i, A in enumerate(lista_compra):
              print(i,A)

     elif valor == 1:
         break
     
     else:
         print('Item nao identificado')