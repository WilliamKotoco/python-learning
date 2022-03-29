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
