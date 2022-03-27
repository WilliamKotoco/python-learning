lista = [1, 2, 3]
lista.append(4)
print(lista)
print()
teste = lista.pop(3)
print(teste)
print(lista)
print()
print("tamanho: {}".format(len(lista)))
print(max(lista))
print(min(lista))
print()
lista2 = [4, 5, 6, 7]
lista.extend(lista2)
print(lista)
print()
lista3 = ["alo", "teste", "testando"]
print("/".join(lista3))
print()
# insert permite colocar qualquer valor em qualquer índice
lista3.insert(2, "manomano")
print(lista3)
print()
