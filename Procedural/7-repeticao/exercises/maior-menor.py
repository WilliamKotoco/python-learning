qtdDeValores = int(input("Quantos valores deseja-se colocar? "))
valores = []
for i in range(qtdDeValores):
    valor = int(input("Digite um valor: "))
    valores.append(valor)
print("{} é o maior valor, enquanto {} é o menor".format(
    max(valores), min(valores)))
