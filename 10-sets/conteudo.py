s1 = set()
s1.add(1)
s2 = {1, 1, 1, 1, 1, 1, 1, 1, 1, }
print(s2)
# um set não vai conter nada repetido
s1.update('teste')
s1.discard('e')
print(s1)
s1.clear()
print(s1)
print()
lista = [1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 123, 432, 64, 65]
listaSemRepeticao = set(lista)
print(listaSemRepeticao)
print()
# comparar se duas listas contém os mesmos elementos caso uma tenha elementos repetidos
lista1 = [1, 1, 1, 1, 3, 4, 5]
lista2 = [1, 3, 4, 5]
if set(lista1) == set(lista2):
    print('São iguais')
