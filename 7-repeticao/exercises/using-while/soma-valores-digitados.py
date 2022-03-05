# Crie um programa que leia números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
acum = 0
numeros = []
while True:
    num = int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    else:
        numeros.append(num)

print("A soma dos números digitados é de {}".format(sum(numeros)))
