#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os X primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo: "))
termos = []
razao = int(input("Digite a razão: "))
qtdTermos = int(input(
    "Digite a quantidade de termos que se deseja calcular: "))
# somando o primeiro termo já imposto com o 0, para calcular os termos
# subsequintes, será necessário adicionar  a quantidade de termos 2
for i in range(qtdTermos):
    termo = a1 + (i) * razao
    termos.append(termo)

print(termos)
