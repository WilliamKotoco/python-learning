qtdFuncionarios = int(input("Quantos funcinários trabalharam essa semana? "))
BateramMetas = []
vendasFuncionarios = []
meta = 10
for i in range(qtdFuncionarios):
    nome = input("Digite o nome do funcinário: ")
    vendas = int(input("Digite o número de vendas: "))

    if vendas > meta:
        BateramMetas.append(nome)
        vendasFuncionarios.append(vendas)
    else:
        pass
print("Os funcionários que bateram a meta são: {}".format(BateramMetas))
for i in range(len(BateramMetas)):
    print("{} vendeu {} ".format(BateramMetas[i], vendasFuncionarios[i]))


def PorcentagemMeta(total, bateramMeta):
    porcentagem = (bateramMeta * 100)/total
    return porcentagem


print("{}% dos funcionários bateram a meta".format(
    PorcentagemMeta(qtdFuncionarios, len(BateramMetas))))
