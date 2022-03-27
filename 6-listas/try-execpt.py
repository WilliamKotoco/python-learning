
try:
    x = "william"
    print(x)
except:
    print("Algo deu errado")
print()
try:
    print(x)
except NameError:
    print("x não está definido")
except:
    print("outro erro")
print()
try:
    print("alo")
except:
    print("n vai ter erro")
else:
    print("sucesso")
