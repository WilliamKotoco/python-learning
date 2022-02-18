# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#  e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
anoNascimento = int(input("Digite o ano de nascimento "))
idade = date.today().year - anoNascimento
if idade < 9:
    print("MIRIM")
elif idade > 9 and idade < 15:
    print("INFANTIL")
elif idade >= 15 and idade < 20:
    print("JÚNIOR")
elif idade >= 20 and idade < 26:
    print("SENIOR")
else:
    print("MASTER")
