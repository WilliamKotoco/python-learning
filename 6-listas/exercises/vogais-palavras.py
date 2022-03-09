#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
qtdPalavras = int(input("Digite a quantidade de palavras a ser digitada: "))


def vogalEmPalavra(palavra):
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    return vogais


for i in range(qtdPalavras):
    palavra = input("Digite a palavra (sem acentos): ")
    print(vogalEmPalavra(palavra))
