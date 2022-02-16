# Checando se bateu a meta ou não2
vendas = int(input("Quantas unidades foram vendidas ?"))
meta = 5000
if (vendas > meta):
    print("Passamos a meta, vendemos {} unidades".format(vendas))
elif vendas == meta*0.5:
    print("Quase passamos a meta, chegamos a metade!")
else:
    print("Não passamos da meta, vendemos {}".format(vendas))
