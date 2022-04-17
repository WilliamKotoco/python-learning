# https://youtu.be/FsAPt_9Bf3U
# https://youtu.be/r7Dtus7N4pI

def funcao1(outra_funcao):
    def organizar(*args, **kwargs):
        print('Começo')
        val = outra_funcao(*args, **kwargs)
        print('fim')
        return val
    return organizar


@funcao1
def funcao2(a, b):
    print(a, b)


@funcao1
def soma(x, y):
    return x+y


print(funcao2('olá', 'senhor'))
print()
print(soma(10, 4))
