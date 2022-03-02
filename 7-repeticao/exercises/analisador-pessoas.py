# : Desenvolva um programa que leia o nome, idade e sexo de x pessoas.
#  No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
#  quantas mulheres têm menos de 20 anos.
nomesMulheres = []
idadesMulheres = []
idadesHomem = []
nomesHomem = []
qtd = int(input("Quantidade de pessoas: "))
for i in range(qtd):
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
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


def MediaGrupo():
    idadesHomem
