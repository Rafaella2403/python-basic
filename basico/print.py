# Falando um pouco sobre a função print

# A função print é usada para imprimir algo na tela, e ela recebe um ou mais argumentos.
print('primeiro argumento')
print(1, 2, 3)

# Ele tem alguns comportamentos padrões, os dois princiais é a separação entre os argumentos e a quebra de linha no final.
# Esses padrões podem ser redefinidos, com os argumentos nomeados:

# No caso do espaço usamos o argumento sep.
print('Rafaella', 'Ribeiro', sep='-')

# Para a quebra de linha usamos o argumento end
# \r\n - CRLF
# \n - LF

print('Nome: ', end='\n')
print('Rafaella')