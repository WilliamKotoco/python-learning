for i in range(5):
    print(i)
print()

produtos = ["coca", "guarana", "vodka", "monster"]
precos = [5, 4, 10, 8]
for i in range(len(produtos)):
    print("{} custa {}".format(produtos[i], precos[i]))
print()
# função enumerate all
for i, item in enumerate(produtos):
    print("Item {}, nome {}".format(i, item))
print()
