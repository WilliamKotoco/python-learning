teste = dict()
teste["teste"] = "retorno"
print(teste)
print("=" * 30)

dados = {'nome': 'josé', 'idade': 14}
print(dados['nome'])
print(len(dados))
print("=" * 30)

del dados['idade']
print(dados)
print("=" * 30)
filme = {
    'nome': 'Star Wars: a new hope',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for chave, valor in filme.items():
    print("o {} é {}".format(chave, valor))
    print("=" * 30)
