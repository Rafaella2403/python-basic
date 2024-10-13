# Try - Tenta executar determinado código
# Except - Se tiver algum erro ele captura

print ('Vou dobrar o número que voce digitar')
numero_string = input('Digite um número: ')

try:
  numero = float(numero_string)

except:
  print('O número digitado é inválido')
  
print(f'O dobro de {numero} é {numero * 2}')