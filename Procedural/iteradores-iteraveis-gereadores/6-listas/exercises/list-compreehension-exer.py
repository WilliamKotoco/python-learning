string = "0123456789" * 6
separacao = 10
listaSeparacaoString = [string[i:i + separacao] for i in range(0,len(string), separacao)]
print(listaSeparacaoString)
print("JUNTANDO:")
print(".".join(listaSeparacaoString))