#  Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
qtdNumeros = int(input("Digite a quantidade de números: "))
for i in range(qtdNumeros):
    numero = int(input("Digite um número: "))
    if numero not in numeros:
        numeros.append(numero)
numeros.sort()
print(numeros)
