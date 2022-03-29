def calcularImposto(valor, taxa):
    imposto = valor * taxa
    return imposto
print(calcularImposto(30, 0.10))
imposto = lambda x,y : x*y
print("Utilizando expressão lambda: {}".format(imposto(30,0.10)))

print()

lista = [
    ['p1',3],
    ['p2',45],
    ['p3',52],
    ['p4',523]
]
# retornar a lista ordenada utilizando funcao lambda
lista.sort(key = lambda item: item[1])
print(lista)