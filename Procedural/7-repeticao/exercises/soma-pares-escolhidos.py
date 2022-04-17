# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
#  que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
qtdPares = 0
for i in range(6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        qtdPares += 1
        soma = soma + num
    else:
        pass
print("A soma dos {} números pares é: {}".format(qtdPares, soma))
