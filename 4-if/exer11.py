# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será
# negado.
valorCasa = int(input("Qual o preço da casa ? "))
SalarioComprador = int(input("Qual salário do comprador? "))
tempoAnual = int(input("Em quantos anos será pago ?"))

qtdMeses = tempoAnual * 12
prestacaoMensal = valorCasa / qtdMeses
if prestacaoMensal < SalarioComprador:
    if prestacaoMensal > SalarioComprador*0.3:
        print("Empréstimo negado!")
    else:
        print('Empréstimo aprovado!')
else:
    print("Salário menor que a prestação, vai pagar como ?")
