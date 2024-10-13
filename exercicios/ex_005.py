'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

valor_digitado = input('Digite um número inteiro: ')

try:
  numero = int(valor_digitado)
  isPar = "é par" if numero % 2 == 0 else "é ímpar"
  
  print(f'O número {numero} {isPar}')
except:
  print('O número informado não é inteiro')
  
