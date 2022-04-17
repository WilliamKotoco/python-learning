produtos = []
while True:
    continuar = int(input('Digite [1] para continuar, [2] para cancelar: '))
    if continuar == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input('Digite o preço: '))
        produtos.append((nome, preco))
    else:
        break
print(produtos)


''' Mostre a soma dos preços utilizando list compreehension'''

total = sum([float(precos) for nome, precos in produtos])
print(f' O preço total da compra é de R${total}')
