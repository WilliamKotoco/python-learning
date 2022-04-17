# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
precoNormal = float(input("Qual o preço de fábrica: "))
pagamento = int(input("[1] para cartão, [2] para dinheiro "))
if pagamento == 1:
    parcelas = int(input("Qual a quantidade de parcelas: "))
    if parcelas == 2:
        preco = precoNormal
    elif parcelas >= 3:
        preco = precoNormal + (precoNormal*0.2 * parcelas)
    else:
        preco = precoNormal - (precoNormal*0.05)
if pagamento == 2:
    preco = precoNormal - (precoNormal*0.1)
print("Preço final foi de {} reais".format(preco))
