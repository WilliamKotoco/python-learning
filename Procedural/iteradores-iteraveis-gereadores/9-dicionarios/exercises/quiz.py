'''
Monte um quiz
'''

acertos = 0
perguntas = {
    'pergunta1': {
        'titulo': 'quanto é 2 + 2',
        'respostas': {'a': 4, 'b': 5, 'c': 34, 'd': 'mordred'},
        'certo': 'a'
    },
    'pergunta2': {
        'titulo': 'quem é o rei da grã-bretanha ?',
        'respostas': {'a': 'arthur', 'b': 'mordred', 'c': 'julio cesar', 'd': 'william de rio preto'},
        'certo': 'd'
    }
}
for key, value in perguntas.items():
    print(f'{key}: {value["titulo"]}')
    for respostaChave, respostaValor in value['respostas'].items():
        print(f'{respostaChave}: {respostaValor}')
    resposta = input("Digite a opção: ")
    if resposta.casefold() == value['certo']:
        print("Parabéns, você acertou!")

        acertos += 1
    else:
        print("errou, a certa era {}".format(value['certo']))
    print()
print("Resultado: {}/{}".format(acertos, len(perguntas)))
