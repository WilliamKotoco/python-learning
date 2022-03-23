# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida. N
# o final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
#  drante o campeonato.
gols = []
jogador = dict()
jogador["nome"] = input("Nome: ")
jogador["qtdPartidas"] = int(input("Quantidade de partidas: "))
for i in range(0, jogador["qtdPartidas"]):
    golPartida = int(input("gols na {}° partida: ".format(1+i)))
    gols.append(golPartida)
jogador["golsPorPartida"] = gols
jogador["totalGols"] = sum(gols)
print(jogador)
