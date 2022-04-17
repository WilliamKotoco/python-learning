x = input("Digite um número menor que 10: ")
x = float(x)
while x < 10:
    if x == 3:
        print()
        x += 1
        continue
    if x - int(x) != 0:
        print("É um número decimal")
        break
    print(x)
    x += 1
