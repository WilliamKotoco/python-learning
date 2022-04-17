
try:
    x = "william"
    print(x)
except:
    print("Algo deu errado")
print()
# ===========================================================================================
try:
    print(y)
except NameError:
    print("y não está definido, linha 9")
except:
    print("vai cair aqui se for outro erro que não NameError")
print()
# ===========================================================================================

try:
    print("alo")
except:
    print("n vai ter erro")
else:
    print("ele vai executar sempre que o bloco try executar")
print()
###############################################
lista = []
try:
    print(lista[1])
except(IndexError, ValueError):
    print("Linha 30: Erro de index ou de valor")
finally:
    print('Vai acontecer sempre, dando certo ou errado')
# o finally é útil quando deve-ser fazer coisas que sempre acontecerão, como
#  fechar conexão com o banco de dados por exemplo
