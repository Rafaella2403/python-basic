# Qual letra mais apareceu nesta frase?

frase = 'Python é uma linguagem de programação poderosa e fácil de aprender, amplamente usada para desenvolvimento web, ciência de dados, automação e muito mais'

# Inicializando as variáveis
qtd_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Remover os espaços para não contar
frase_sem_espacos = frase.replace(' ', '').lower()

# Loop para contar a frequência de cada letra
for letra_atual in set(frase_sem_espacos):
    qtd_atual = frase_sem_espacos.count(letra_atual)
    
    if qtd_mais_vezes < qtd_atual:
        qtd_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

print(f'A letra "{letra_apareceu_mais_vezes}" apareceu {qtd_mais_vezes} vezes.')