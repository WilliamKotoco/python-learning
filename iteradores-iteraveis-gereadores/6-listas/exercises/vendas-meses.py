meses = ["jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dez"]
vendas_1semestre = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2semestre = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_1semestre.extend(vendas_2semestre)

indexMaiorVenda = vendas_1semestre.index(max(vendas_1semestre))
indexMenorVenda = vendas_1semestre.index(min(vendas_1semestre))

print("O mês de maior venda foi o {}, vendendo {} unidades"
      .format(meses[indexMaiorVenda], max(vendas_1semestre)))
print("O mês de menor venda foi o {}, vendendo {} unidades"
      .format(meses[indexMenorVenda], min(vendas_1semestre)))
print("O faturamento total foi de {}".format(sum(vendas_1semestre)))
