#: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# Maneira 1 de fazer: Assumindo
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
maior = num2
if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num2 and num3 > num1:
    maior = num3
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))

# Maneira 2: utilizando as próprias funções do python
print("==" * 20)
numeros = [num1, num2, num3]
print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))
