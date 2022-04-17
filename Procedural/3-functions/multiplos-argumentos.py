
def funcao(*args):
    print(args)


# O resultado vai ser uma tupla
print(funcao(1, 3, 5, 5, 3, 6))

lista = [1, 2, 3, 4, 5]
# desempacotamento de uma lista e mandando os valores para dentro da tupla dos argumentos
print(funcao(*lista))
print()
# se quiser transformar a tupla em lista:

# kwars manda os argumentos em forma de dicionário


def funcao2(*args, **kwargs):
    listArgs = list(args)
    idade = kwargs.get('idade')
    print(kwargs['nome'], idade)


print(funcao2(1, 3, 4, 5, 35, 235, nome='lulz', idade=14))
