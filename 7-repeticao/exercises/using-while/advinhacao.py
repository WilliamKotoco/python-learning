# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
user = 11
tentativas = 0
while user != computador:
    user = int(input("Escolha um número: "))
    tentativas += 1
print("Parabéns, conseguiu após {} tentativas".format(tentativas))
