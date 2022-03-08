#  Crie uma tupla preenchida com os 10 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do fluminense.
times = ('Atletico', 'flamengo', 'palmeiras', 'fortaleza', 'corinthians',
         'bragantino', 'fluminense', 'america', 'atletico go', 'santos')
print("Os cinco primeiros colocados são: {}\n".format(times[0:5]))

print("Os quatro últimos colocados são {}\n".format(times[-4:]))

print("Em ordem alfabética: {}\n".format(sorted(times)))

print("O fluminense está ná {} posição\n".format(times.index('fluminense') + 1))
