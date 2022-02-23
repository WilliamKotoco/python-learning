
try:
    x = "william"
    print(x)
except:
    print("Algo deu errado")
print("=====" * 20)
try:
    print(x)
except NameError:
    print("x não está definido")
except:
    print("outro erro")
print("=====" * 20)
try:
    print("alo")
except:
    print("n vai ter erro")
else:
    print("sucesso")
