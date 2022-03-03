# : Desenvolva um programa que leia o nome, idade e sexo de x pessoas.
#  No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
#  quantas mulheres têm menos de 20 anos.
from statistics import mean


nomesMulheres = []
idadesMulheres = []
idadesHomem = []
nomesHomem = []
qtd = int(input("Quantidade de pessoas: "))
for i in range(qtd):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = int(input("Digite o sexo [1] masculino, [2] feminino: "))
    if sexo == 1:
        nomesHomem.append(nome)
        idadesHomem.append(idade)
    elif sexo == 2:
        nomesMulheres.append(nome)
        idadesMulheres.append(idade)


def OlderMan():
    indexMaisVelho = idadesHomem.index(max(idadesHomem))
    nomeMaisVelho = nomesHomem[indexMaisVelho]
    return nomeMaisVelho


def mulheresMenos20y():
    acum = 0
    for i in range(len(idadesMulheres)):
        if idadesMulheres[i] < 20:
            acum += 1
        else:
            pass
    return acum


def MediaGrupo():
    idadesHomem.extend(idadesMulheres)
    media = mean(idadesHomem)
    return media


print("O homem mais velho é: {} \n a média das idades é {} \n há {} mulheres com menos de 20 anos".
      format(OlderMan(), MediaGrupo(), mulheresMenos20y()))
