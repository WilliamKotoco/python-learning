filme = {
    'nome': 'Star Wars: a new hope',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(len(filme))
print("=" * 30)
print('ano' in filme)
print("=" * 30)
print(1977 in filme.values())
print("=" * 30)

# Função para encontrar um item correspondente a um valor


def reverseLookup(dicionario, valor):
    for i in dicionario:
        if dicionario[i] == valor:
            return i


print(reverseLookup(filme, 1977))
print("=" * 30)
copia = filme.copy()
print(copia)
print("=" * 30)
filme.clear()
print(filme)
