"""
Exemplo básico de uma calculadora usando while.
Peça dois números para o usuário, caso ele digite um valor inválido uma mensagem
deve ser apresentanda para o usuário pedindo pra ele digitar um número válido.
Em seguinda ele tem que selecionar um operador sendo eles, soma, subtração, multiplicação
ou divisão.
"""

# Função responsável solicitar e validar o número digitado
def solicitar_numero(mensagem):
  while True:
    valor = input(mensagem)
    try:
      return float(valor)
    except:
      print('Por favor, digite um número válido.')
      
# Função responsável por solicitar o operador e realiza a operação
def realiza_operacao (numero_1, numero_2):
  while True:
    operador = input('\nInforme um operador: ')
    if operador == 'som':
      return numero_1 + numero_2
    elif operador == 'sub':
      return numero_1 - numero_2
    elif operador == 'mult':
      return numero_1 * numero_2
    elif operador == 'div':
      return numero_1 / numero_2
    else:
      print('Por favor, digite um operador válido.')

# Solicitando os dois números
numero_1 = solicitar_numero("Digite o primeiro número: ")
numero_2 = solicitar_numero("\nDigite o segundo número: ")

# Selecionando o operador
print('\nSelecione um operador, sendo:')
print('som - soma')
print('sub - subtracao')
print('mult - multiplicacao')
print('div - divisão')
resultado = realiza_operacao(numero_1, numero_2)

print(f"O resultado da operação é {resultado}")