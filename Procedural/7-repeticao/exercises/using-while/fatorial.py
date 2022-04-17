# Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input("Digite um número para calcular seu fatorial: "))
contador = num
fatorial = 1
while contador > 0:
    print("{}".format(contador), end="")
    print(" x "if contador > 1 else " = ", end="")
    fatorial *= contador
    contador = contador - 1
print(fatorial)
