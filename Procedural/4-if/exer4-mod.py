# check if a number is even or not
num = input("Digite um número")
if num:
    num = int(num)
    if (num % 2) == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
else:
    print("Digite o número")
