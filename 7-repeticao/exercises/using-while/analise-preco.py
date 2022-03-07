#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
gastoTotal = 0
qtdProdutosMaiores100 = 0
listaProdutos = []
listaPrecos = []
while True:
    produto = input("Digite o nome do produto: ")
    listaProdutos.append(produto)
    preco = int(input("Digite o preço: "))
    listaPrecos.append(preco)
    if preco > 1000:
        qtdProdutosMaiores100 += 1
    parada = input(
        "Digite [F] para finalizar ou [A] para adicionar mais produtos: ")
    if parada.casefold() == 'f':
        break


def maisBarato():
    PrecomenorProduto = listaPrecos.index(min(listaPrecos))
    maisBarato = listaProdutos[PrecomenorProduto]

    return maisBarato


print("Total: {}".format(sum(listaPrecos)))
print("Há {} produtos mais caros que 1000".format(qtdProdutosMaiores100))
print("O produto mais barato é {}".format(maisBarato()))
