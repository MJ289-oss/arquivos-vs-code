nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome == '' and idade == '':
    print('\nvocê deixou campos vazios')

else:
 print(f'\nSeu nome é: {nome}')
 print(f'Seu nome invertido é: {nome[::-1]}')
 if ' ' in nome:
  print('seu nome contém espaços')
 else:
   print('Seu nome não tem epaços')
 print(f'seu nome tem: {len(nome)} letras')
 print(f'A primeira letra do seu nome é: {nome[0]}')
 print(f'A ultima letra do seu nome é: {nome[-1]}')