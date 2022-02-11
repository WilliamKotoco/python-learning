# Jogo do azar
from binascii import crc32
from random import randint
from time import sleep
import winsound
slot = randint(0, 5)
tentativa = int(input("Qual slot, dentre os 5, você deseja colocar ? "))
print("===" * 20)
sleep(5)
print("RODANDO A ARMA....")
sleep(5)
print("===" * 20)
if tentativa == slot:
    print("Bem vindo ao inferno")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
else:
    print("Você está vivo")
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


# Amanhã vou tentar colocar som de tiro dentro do if
