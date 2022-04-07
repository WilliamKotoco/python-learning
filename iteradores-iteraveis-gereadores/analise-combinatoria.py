''' Aula básica de matemática
Combinações -> a ordem não importa e não repete valores únicos
Permutações -> A ordem importa e não repete valores únicos
Produto -> a ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product

pessoas = ['João', ' Maria', 'José', 'Carlos']  # sem criatividade

for grupo in combinations(pessoas, 2):  # combinar pessoas em grupos de dois
    print(grupo)
print('{:%^100}'.format('PERMUTAÇÕESs'))
for grupo in permutations(pessoas, 2):
    print(grupo)
print('{:%^100}'.format('PRODUTO'))
for grupo in product(grupo, repeat=2):
    print(grupo)
