# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# . No final, mostre a matriz na tela, com a formatação correta.
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
somaPar = somaColuna3 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha} ,{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()


print("A soma dos valore pares é : {}".format(somaPar))
for linha in range(0, 3):
    somaColuna3 += matriz[linha][2]
print("A soma dos valores da terceira coluna é de {}" .format(somaColuna3))
print("O maior valor da segunda linha é {}" .format(max(matriz[1])))
