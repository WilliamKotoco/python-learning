# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se
# já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou
#  que passou do prazo.
from datetime import date
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = date.today().year
if anoAtual - anoNascimento == 18:
    print("Você deve se alistar esse ano, acesse ao: ")
    print("https://alistamento.eb.mil.br")
elif anoAtual - anoNascimento < 18:
    print("Falta(m) {} ano(s) para seu alistamento".format(
        18 - (anoAtual - anoNascimento)))
else:
    print("Você deveria ter se alistado há {} anos".format(
        -1*(18 - (anoAtual - anoNascimento))))
