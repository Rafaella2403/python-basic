"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
  Exiba:
    Seu nome é {nome}
    Sue nome invertido é {nome_invertido}
    Se o nome contém ou não espaços
    Seu nome tem {n_letras} letras
    A primeira letra do seu nome é {primeira_letra}
    A última letra do seu nome é {ultima_letra}
Se nada for digitado em nome ou idade: 
  Exiba:
    Desculpe, você deixou campos vazios.
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
  nome_invertido = nome[::-1]
  n_letras = len(nome.replace(' ', ''))
  primeira_letra = nome[0]
  ultima_letra = nome[-1]
  contem_espacos = "contém" if " " in nome else "não contém"
  
  print(f'Seu nome é {nome}')
  print(f'Sue nome invertido é {nome_invertido}')
  print(f'O nome {contem_espacos} espaços')
  print(f'A primeira letra do seu nome é {primeira_letra}')
  print(f'A última letra do seu nome é {ultima_letra}')
  
else:
  print('Desculpe, você deixou campos vazios.')