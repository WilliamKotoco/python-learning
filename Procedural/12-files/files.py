# https://docs.python.org/3/library/functions.html#open
import os


try:
    file = open('arquivo.txt', '+w')
    file.write("Essa é a primeira linha, feita primeiramente porque é a primeira")
    file.write('\n Essa é a segunda ilnha, feita segundamente porque é a segunda')

    # voltando o cursor para o inicio
    # file.seek(0, 0)
    # for linha in file:
    # print(linha)
except Exception as e:
    print('files.py, linha 11: {}'.format(e))

# finally:
    # file.close()

# outra maneira de fazer
with open('12-files/arquivo.txt', '+a'):
    file.write("\nútlima linha, prometo")
    file.seek(0, 0)
    print(file.read())
    file.close()

fechar = int(
    input("Digite [3] para apagar o arquivo, outro número para não apagar: "))
if fechar == 3:
    os.remove('12-files/arquivo.txt')
else:
    print('Ok então')
