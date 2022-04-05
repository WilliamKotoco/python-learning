# se tiver o tipo __iter()__, é um objeto iterável
# se o botável no loop for também é iterável
nums = [1, 2, 3]
print(hasattr(nums, '__iter__'))

iteradorNums = nums.__iter__()  # iter(nums) é a melhor maneira de fazer
print(type(iteradorNums))
print()

# um iterador lembra ONDE ele está durante a iteraç
print(next(iteradorNums))
print(next(iteradorNums))
print(next(iteradorNums))

print()
# geradores (aparição do yield)


def squareNumbers(num):
    for i in num:
        yield i**2


numbersTesting = squareNumbers([1, 2, 3, 4, 5])
print(numbersTesting)  # geradores não guardam o resultado inteiro na memória
print(next(numbersTesting))
print()
for i in numbersTesting:
    print(f'{i} ', end='')
