
# funcionamento da função zip

from itertools import count, zip_longest


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
unindo = zip(lista1, lista2)
for i in unindo:
    print(i)

# função ziplongest (importado)
unindo2 = zip_longest(lista1, lista2, fillvalue='Número')
for k in unindo2:
    print(k)
print()
# a função count da um contador infinito, muito útil para esse exemplo
nomes = ['João', 'Carlos', 'Maris', 'Stella']
ids = count()
tabela = zip(nomes, ids)
print(list(tabela))
