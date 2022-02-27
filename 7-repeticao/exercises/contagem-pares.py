#  Crie um programa que mostre na
#  tela todos os números pares que estão no intervalo entre 1 e x.
limite = int(input("Qual limite ? "))
for i in range(limite):
    if i % 2 == 0:
        print(i)
    else:
        pass
