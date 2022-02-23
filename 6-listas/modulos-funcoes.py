lista = [1, 2, 3]
lista.append(4)
print(lista)
print("=====" * 20)
teste = lista.pop(3)
print(teste)
print(lista)
print("=====" * 20)
print("tamanho: {}".format(len(lista)))
print(max(lista))
print(min(lista))
print("=====" * 20)
lista2 = [4, 5, 6, 7]
lista.extend(lista2)
print(lista)
print("=====" * 20)
lista3 = ["alo", "teste", "testando"]
print("/".join(lista3))
