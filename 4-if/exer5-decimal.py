# receba um número e retorne a parte decimal dele. Caso não tenha, informe que é um número inteiro
num = input("Digite um número")
int()
if num.isdigit():
    num = float(num)
    if num - int(num) == 0:
        print("É um numero inteiro")
    else:
        print("é decimal")
else:
    print("O que foi digitado não é um número!")
