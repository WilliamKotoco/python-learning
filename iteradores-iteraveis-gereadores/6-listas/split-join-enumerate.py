string = "eu tenho 45 anos, moro em ilha solteira"
# o split divide uma string em uma lista seprando a partir da virgula

lista = string.split(',')
print(lista)

# o join vai juntar os elemtnos de uma lista a partir de um caractere
string2 = ','.join(lista)
print(string2)
print()
# enumerate: percorra uma lista e, ao mesmo tempo, tenha em uma varíavel o índice daquele item. retorna em tupla
listaFuncionarios = ["João", "Carlos", "Maria"]
listaSalarios = [1500, 3000, 2000]
for i, funcionario in enumerate(listaFuncionarios):
    print(f'{funcionario} ganha {listaSalarios[i]}')
print()
# desempacotamento de listas
numeros = [1, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# *nome cria uma lista com detemrinado nome que vai armazenar o resto
n1, n2, n3, *restante, ultimo = numeros
print(n2)
print(restante)
print(ultimo)
