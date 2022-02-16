# Função: Sequência de declarações que podem performar uma computação
# Ela tem um nome e uma sequência de declarações. Ela pode ser chamada posteriormente por
# esse nome. Uma função vai receber um argumento e retornar um resultado, sendo o argumento opcional e o
# resultado podendo ser nulo.
# uma variável criada dentro de uma função só vai existir dentro da função

# Vantagens da função:
# - deixa o código mais fácil de ler e debugar
# - faz um código menor, eliminando redundância
# - uma função, quando bem escrita, pode ser reutilizada em outros programas.
import math


# funções de converter valores
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
