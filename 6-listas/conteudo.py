nome = "william"
carlao = ["carlos do fut", "carlos do volei"]
nomes = [nome, "jao", "das coxinhas", carlao, "teste"]
print(nomes)
print("======================================" * 3)
print(nomes[3])
print("======================================" * 3)
print(nomes[2:5])
print("==============================================" * 3)
nomes[2] = "roberto"
print(nomes)
print("==================================================" * 3)
# mudando varios elementos de uma vez
nomes[1:3] = ['teste', 'teste']
print(nomes)
