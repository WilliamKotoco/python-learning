# exemplo sem list compreehension:
symbols = "@#$%"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# utilizando list compreehension: bem melhor
symbols = "@#$%"
codes = [ord(symbol) for symbol in symbols]
print(codes)

'''
Se a listcomprehension usar mais de duas linhas, é melhor fazer da maneira tradicional com for loop mesmo.
'''
lista = list(range(1, 11))
exemplo2 = [(x,y) for x in lista for y in range(3)]
print(exemplo2)