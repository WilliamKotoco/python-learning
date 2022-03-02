# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
frase = input("Digite uma frase: ")
frase.casefold()
frase.replace(" ", "")
if frase == frase[::-1]:
    print("É um palindromo")
else:
    print("Não é  um palindromo")
