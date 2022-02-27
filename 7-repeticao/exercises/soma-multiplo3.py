#  Faça um programa que calcule a soma entre todos os números que são múltiplos
#  de três e que se encontram no intervalo de 1 até x.
limite = int(input("Qual o limite ? "))
soma = 0
multiplos = 0
for i in range(limite):
    if i % 3 == 0:
        if i % 2 != 0:
            multiplos = multiplos + 1
            soma = soma + i
    else:
        pass
print("A soma dos {} valores é {}".format(multiplos, soma))
