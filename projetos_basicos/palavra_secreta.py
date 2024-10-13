import random

animais = ['vaca', 'cachorro', 'gato', 'cavalo', 'coelho', 'leao', 'tigre', 'elefante', 'girafa', 'raposa']
objetos = ['mesa', 'cadeira', 'computador', 'celular', 'lapis', 'caneta', 'relogio', 'livro', 'garrafa', 'mochila']
frutas = ['maca', 'banana', 'laranja', 'uva', 'morango', 'melancia', 'abacaxi', 'pera', 'limao', 'manga']
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco', 'rosa', 'roxo', 'marrom', 'cinza']
paises = ['brasil', 'argentina', 'espanha', 'franca', 'italia', 'canada', 'mexico', 'japao', 'china', 'alemanha']

print('Vamos brincar: ')
print('\nPrimeiro vamos para as regras:')
print('1 - Selecione uma categoria.')
print('2 - Digite uma letra.')
print('3 - O jogo vai dizer se a letra está ou não na palavra.')
print('4 - Você pode tentar adivinhar a palavra ou continuar.')
print('\nCategorias disponíveis: ')
print('a - animal')
print('o - objetos')
print('f - frutas')
print('c - cores')
print('p - paises')

def seleciona_categoria():
    while True:
        categoria = input('Selecione uma categoria: ')
        if categoria == 'a':
            return random.choice(animais)
        elif categoria == 'o':
            return random.choice(objetos)
        elif categoria == 'f':
            return random.choice(frutas)
        elif categoria == 'c':
            return random.choice(cores)
        elif categoria == 'p':
            return random.choice(paises)
        else:
            print('Selecione uma categoria válida.')


def seleciona_letra():
    while True:
        letra = input('Escreva uma letra: ').lower()
        if len(letra) != 1 or not letra.isalpha():
            print('Informe apenas uma letra válida.')
        else:
            return letra


def valida_letra(palavra_secreta, letras_acertadas):
    resultado = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            resultado += letra
        else:
            resultado += '*'
    return resultado


palavra_secreta = seleciona_categoria().lower()
letras_acertadas = []
tentativas = 0
palavra_oculta = ['*' for _ in palavra_secreta]

while True:
    print(f"\nPalavra secreta: {valida_letra(palavra_secreta, letras_acertadas)}")

    letra = seleciona_letra()

    tentativas += 1

    if letra in palavra_secreta:
        if letra not in letras_acertadas:
            letras_acertadas.append(letra)
        print(f"A letra '{letra}' está na palavra!")
        print(f"Palavra secreta: {valida_letra(palavra_secreta, letras_acertadas)}")
    else:
        print(f"A letra '{letra}' não está na palavra.")
    
    if valida_letra(palavra_secreta, letras_acertadas) == palavra_secreta:
        print(f"\nParabéns! Você acertou a palavra '{palavra_secreta}' em {tentativas} tentativas!")
        break
    
    continuar = input("Você deseja tentar adivinhar a palavra completa? (s/n): ").lower()
    
    if continuar == 's':
        tentativa_palavra = input("Digite a palavra completa: ").lower()
        if tentativa_palavra == palavra_secreta:
            print(f"\nParabéns! Você acertou a palavra '{palavra_secreta}' em {tentativas} tentativas!")
            break
        else:
            print(f"Palavra incorreta. Continue tentando.")
