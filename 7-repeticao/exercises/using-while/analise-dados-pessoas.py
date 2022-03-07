# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# o final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
contadorIdade = 0
qtdHomens = 0
qtdMulheresMenores20 = 0
while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("F para feminino, M para masculino: ")
    if idade > 18:
        contadorIdade += 1
    if sexo.capitalize() == "M":
        qtdHomens += 1
    if sexo == "F" and idade < 20:
        qtdMulheresMenores20 += 1
    parada = input(
        "Digie [A] para adicionar mais um usuário, digite [F] se finalizou: ")
    parada.casefold()
    if parada == 'f':
        break
print("Há {} maiores de 18, {} homens e {} mulheres menores que 20".format(
    contadorIdade, qtdHomens, qtdMulheresMenores20))
