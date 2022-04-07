
pessoas = ['joao', 'carlos', 'carosi', 'jotape', 'alo', 'nome3', 'semnome',
           'mudinho', 'falador', 'surdo', 'ReiDelas', 'quatorze', 'catorze']

produtos = [{'nome': 'Acarajé', 'preço': 33},
            {'nome': 'Pata tubarão', 'preço': 234},
            {'nome': 'ventilador coringa', 'preço': 15},
            {'nome': 'excalibur', 'preço': 9999},
            {'nome': 'biblia satanica', 'preço': 32},
            {'nome': 'estatua jesus', 'preço': 0.5},
            {'nome': 'oculos kurt cobain', 'preço': 13},
            {'nome': 'mascara batman', 'preço': 90},
            {'nome': 'misterio', 'preço': 10},
            {'nome': 'lapis', 'preço': 2}]


lista = list(range(10))
# mapa pega uma função e um iterável e devolve um iterador que aplica a função para cada item do iterável
listaAoQuadrado = map(lambda x: x**2, lista)
for i in listaAoQuadrado:
    print(i)

print(produtos)
print()
