# Podemos utilizar módulos dentro do python. Um módulo, ou biblioteca, é um arquivo que
# contém várias funções dentro dele. Olhar na documentação.

from math import sin
import math
from winsound import *
x = math.pi
print(x)

# para não termos que usar o prefixo math., podemos importar apenas o que iremos usar ou podemos importar
# a biblioteca inteira colocando um *. Irei testar utilizando a biblioteca winsound
PlaySound("SystemExit", SND_ALIAS)

# como demos um import sin from math, podemos utilizar apenas a função seno sem ter que colocar
# o prefixo math.
print(sin(30))
