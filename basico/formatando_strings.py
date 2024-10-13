nome = 'Rafaella Ribeiro'
altura = 1.75
peso = 92.5

# Formatando strings usando método format 
print('{0} tem {1} de altura e pesa {2}'.format(nome, altura, peso))

# Formatando strings com interpolação
print(
  '%s tem %.2f de altura e pesa %f'
  % (nome, altura, peso)
)

# Formatando strings usando f-strings

'''
Anotações básicas sobre formatação de strings

Para adicionar variáveis a string colocamos logo após o
% a letra correspondente ao tipo da variável.

%s - string
%d - int
%f - float

Para limitar o número de casas decimais usamos:
%.<numero de casas>f

Para adicionar caracteres a string usamos:
{variavel: >10} - esquerda
{variavel: <10} - direta
{variavel: ^10} - centro

Para transformar em hexadecimal
(caractere)(><^)(quantidade)

Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel: >10}')