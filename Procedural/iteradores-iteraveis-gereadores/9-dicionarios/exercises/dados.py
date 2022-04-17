#  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
#  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
values = []
for i in range(0, 4):
    value = randint(1, 6)
    values.append(value)
values.sort(reverse=True)
resultado = {"jogador1": values[0], "jogador2": values[2],
             "jogador3": values[1], "jogador4": values[3]}
print(resultado)
