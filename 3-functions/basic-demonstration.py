# funções de converter valores
import math
print(type(32))
print(int(3.4))
print(float(32))
print(float('40.4'))
print(str(30))

# Algumas funções matemáticas
print(math.sin(45))
print(math.pi)


# sintaxe para criação da própria função


def teste():
    print("Testando função sem parâmetro")
    print("===" * 5)


def soma(x, y):
    soma = x+y
    print(soma)


print(teste())
print(soma(7, 3))
