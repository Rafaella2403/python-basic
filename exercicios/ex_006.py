"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex:
  0-11 > Bom dia
  12-17 > Boa tarde
  18-23 > Boa noite
"""

valor_digitado = input('Digite as horas: ')

try:
  horas = int(valor_digitado)
  if horas == 0 and horas <= 11:
    print('Bom dia')
  elif horas == 12 and horas <=17:
    print('Boa tarde')
  else:
    print('Boa noite')
  
except:
  print('Hora informada é inválida')