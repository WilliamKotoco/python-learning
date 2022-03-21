# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
#  de cada aluno individualmente.
qtdAlunos = int(input("Quantos alunos há de ser cadastrados ? "))
nomes = []
notas1 = []
notas2 = []
medias = []
for i in range(qtdAlunos):
    nome = input("Digite o nome: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    medias.append((notas1[i] + notas2[i])/2)

for i in range(qtdAlunos):
    print("{} tem a média de {}".format(nomes[i], medias[i]))
