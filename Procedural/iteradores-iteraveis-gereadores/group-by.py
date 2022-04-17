from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]
# ordenando notas:
# é necessário essa função para fazer com que ele ordene só a nota, não o dicionário inteiro
alunos.sort(key=lambda x: x['nota'])
alunos_agrupados = groupby(alunos, lambda x: x['nota'])

for chave, valor in alunos_agrupados:
    v1, v2 = tee(valor)
    print(f'Alunos que tiraram {chave}, {len(list(v2))}')
    for i in v1:
        print(i['nome'])
    print()
