# Você pode colocar uma função dentro da outra sem nenhum problema.

# print(print_lyrics())
# não tem como rodar a função antes de declarar ela.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("Cause if you stay i would even wait all night")
    print("Or until my heart explodes")


# def repeat_lyrics():
 #   print_lyrics()
#    print_lyrics()

print(repeat_lyrics())
# Evite declarar uma função que precise de uma outra função antes da função necessitada. Mas caso aconteça
# não vai dar problema
