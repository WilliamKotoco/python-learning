# Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
qtdNumeros = int(input("Digite a quantidade de números a ser digitada: "))
numeros = []
numerosPares = []
numerosImpares = []
for i in range(qtdNumeros):
    numero = int(input("Digite o número: "))
    numeros.append(numero)


def getParNumeros():
    for i in range(qtdNumeros):
        if numeros[i] % 2 == 0:
            numerosPares.append(numeros[i])
        else:
            pass
    return numerosPares


def getImparNumeros():
    for i in range(qtdNumeros):
        if numeros[i] % 2 != 0:
            numerosImpares.append(numeros[i])
        else:
            pass
    return numerosImpares


print(numeros)
print(getImparNumeros())
print(getParNumeros())
