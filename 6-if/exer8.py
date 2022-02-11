#: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = input("Qual a distância da viagem ? ")
if dist:
    dist = int(dist)
    if dist < 200:
        preco = dist * 0.5
        print("O preço será de {} reais".format(preco))
    else:
        preco = dist * 0.45
        print("O preço será de {} reais".format(preco))
else:
    print("Digite uma distância")
