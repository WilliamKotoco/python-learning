venda = [100, 400, 523, 643, 64, 57, 523235, 56, 53, 6]
meta = 200
funcionarios = ["Joao", "Carlos", "Folio", "Roberto",
                "Maria", "Sla", "Março", "A", "O", "i"]
i = 0
while i < len(venda):
    if venda[i] > meta:
        print("O funcionário {} bateu a meta ".format(funcionarios[i]))
    else:
        pass
    i = i + 1
