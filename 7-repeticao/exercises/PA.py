#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os X primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo: "))
termos = [a1]
razao = int(input("Digite a razão: "))
qtdTermos = int(input(
    "Digite a quantidade de termos que se deseja calcular: "))
for i in range(qtdTermos):
    termo = (a1 + razao) * i
    termos.append(termo)

print(termos)
