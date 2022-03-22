# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.]
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime


dados = dict()
dados["nome"] = input("Digite o nome: ")
dados["anoNascimento"] = int(input("Digite o ano de nascimento: "))
date = datetime.date.today()
year = date.strftime("%Y")
idade = int(year) - dados["anoNascimento"]
dados["CPTS"] = int(input("Carteira de trabalho (digite 0 caso não tenha): "))
if dados["CPTS"] != 0:
    dados["anoContratação"] = int(input("Digite o ano de contratação: "))
    dados["salário"] = int(input("Digite o salário: "))
    anosTrabalhados = int(year) - dados["anoContratação"]
    anoAposentadoria = int(year) + (35 - anosTrabalhados)
else:
    pass
print(dados)
print()
if dados["CPTS"] != 0:
    print("Irá se aposentar em {} com {} anos".format(
        anoAposentadoria, anoAposentadoria - dados["anoNascimento"]))
