for i in range(5):
    print(i)
print("===================================" * 3)

produtos = ["coca", "guarana", "vodka", "monster"]
precos = [5, 4, 10, 8]
for i in range(len(produtos)):
    print("{} custa {}".format(produtos[i], precos[i]))
print("===================================" * 3)
# função enumerate all
for i, item in enumerate(produtos):
    print("Item {}, nome {}".format(i, item))
