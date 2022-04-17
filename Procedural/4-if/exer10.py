#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual seu salário: "))
if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print("Seu salário salário foi reajustado para o valor de {}".format(aumento))
