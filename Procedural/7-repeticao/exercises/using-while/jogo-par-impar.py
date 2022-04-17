# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
userChoice = input("Par ou ímpar ? ")
userChoice.casefold()
vitorias = 0
if userChoice == "par":
    computer = "ímpar"
else:
    computer = "par"
while True:
    user = int(input("Digite um número: "))
    computer = randint(1, 10)
    print("O computador escolheu {}".format(computer))
    print(user + computer)
    if (user + computer) % 2 == 0 and userChoice == "par":
        print("Usuário venceu")
        vitorias += 1
    elif (user + computer) % 2 != 0 and userChoice == "ímpar":
        print("Usuário venceu")
        vitorias += 1
    elif (user + computer) % 2 == 0 and userChoice == "ímpar":
        break
    else:
        break
print("FIM")
print("Houve um total de {} vitórias".format(vitorias))
