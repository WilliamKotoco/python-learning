qtdPerguntas = int(input('Quantas perguntas deseja colocar: '))
acertos = 0
listadicionarios = []
for i in range(qtdPerguntas):
    pergunta = dict()
    pergunta['titulo'] = input("Pergunta: ")
    pergunta['opcoes'] = dict()
    pergunta['opcoes']['A'] = input("Opção A: ")
    pergunta['opcoes']['B'] = input("Opção B: ")
    pergunta['opcoes']['C'] = input("Opção C: ")
    pergunta['opcoes']['D'] = input("Opção D: ")
    pergunta['certa'] = input('Opção certa: ')
    listadicionarios.append(pergunta)
print("=====================" * 20)
print("Agora passe o computador para outra ")
for dicionario in listadicionarios:

    print('Pergunta: {}'.format(dicionario['titulo']))
    for k, v in dicionario['opcoes'].items():
        print('{} {}'.format(k, v))
    opcao = input('Digite a opção: ')
    if opcao.capitalize() == dicionario['certa'].capitalize():
        print("Parabéns, você acertou!")
        acertos += 1
    else:
        print("Errou")
    print()
print("Resultado: {}/{}".format(acertos, qtdPerguntas))
