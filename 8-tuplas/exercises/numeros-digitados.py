# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = tuple(int(input("Digite os números: ")) for i in range(1, 5))
print("O número 9 apareceu {} vezes!\n".format(numeros.count(9)))
print("O primeiro valor 3 está na {} posição\n".format(numeros.index(3) + 1))
print("Os números pares são {}\n".format({n for n in numeros if n % 2 == 0}))
