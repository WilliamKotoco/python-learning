# Fundo de investimento
# Caso o fundo não entregue 5% de retorno, ele não pode cobrar de seus investidores
# Caso ele entregue mais de 5% de retorno, ele cobra uma taxa de 2%
# Caso entregue mais de 20%, cobrará de 4%
meta = 0.05
investido = int(input("Quanto foi o valor investido ?"))
renda = int(input("Quanto foi a renda ?"))
if (renda == investido + (investido * 0.05)):
    taxa = renda * 0.02
    lucro = renda - (investido + taxa)
    print("Sua renda é de {}cruzeiros. Foi cobrado uma taxa de 2% ({})".format(lucro, taxa))
elif (renda > investido + (investido * 0.2)):
    taxa = renda * 0.04
    lucro = renda - (investido + taxa)
    print("Sua renda é de {} cruzeiros. Foi cobrado uma taxa de 4% ({})".format(
        lucro, taxa))
else:
    taxa = 0
    lucro = renda - (investido + taxa)
    print("Sua renda é de {}cruzeiros".format(lucro))
