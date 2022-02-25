produto = input("Digite o produto. Se não houver, digite enter vazio: ")
listaProdutos = []
listaProdutos.append(produto)
while listaProdutos[-1] != "":
    produto = input("Digite o produto. Se não houver, digite enter vazio: ")
    listaProdutos.append(produto)
print("Foram adicionados {}".format(listaProdutos))
