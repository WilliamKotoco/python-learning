def divisao(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Não tem como dividir por zero!")
    if n1.isnumeric() == False:
        raise TypeError("Não foi digitado um número")
    return n1/n2


# print(divisao(3, 0))
print()
print(divisao('a', 3))
