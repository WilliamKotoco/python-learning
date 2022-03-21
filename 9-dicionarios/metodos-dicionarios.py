filme = {
    'nome': 'Star Wars: a new hope',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(len(filme))
print('ano' in filme)
print(1977 in filme.values())

# Função para encontrar um item correspondente a um valor


def reverseLookup(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i


print(reverseLookup(filme, 1977))
