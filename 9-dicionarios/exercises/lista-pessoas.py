# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
from statistics import mean


listaPessoas = []
mulheres = []
idades = []
idadesAcimaMedia = []
while True:
    pessoa = dict()
    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade: "))
    idades.append(pessoa["idade"])

    if pessoa["idade"] > mean(idades):
        idadesAcimaMedia.append(pessoa["idade"])

    pessoa["sexo"] = input('Sexo [M] masculino [F] feminino: ')
    if pessoa["sexo"].capitalize() == "F":
        mulheres.append(pessoa["nome"])
    listaPessoas.append(pessoa)
    continuar = int(
        input("Digite 999 para parar ou digite 1 para continuar: "))
    if continuar == 999:
        break

    else:
        pass
print("Foram cadastrados {} pessoas".format(len(listaPessoas)))
print("As mulheres são: {}".format(mulheres))
print("As idades acima da média são {}".format(idadesAcimaMedia))
