# O usuário vai digitar dois números e o terminal vai apresentar se o primeiro valor
# é maior que o segundo valor.

numero_1 = input('Digite o primeiro valor: ')
numero_2 = input('Digite o segundo valor: ')

if numero_1 > numero_2:
  print(f'O número {numero_1} é maior que o número {numero_2}')
elif numero_1 == numero_2:
  print(f'O número {numero_1} é igual ao número {numero_2}')
else:
  print(f'O número {numero_1} é menor que o número {numero_2}')