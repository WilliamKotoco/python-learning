'''
Crie uma função que receba uma função2 como parâmetro e retorne o valor dela executado. Faça
a função1 executar duas funções que recebam diferentes números como argumentos
'''


def saudacao(funcao2, *args, **kwargs):
    return funcao2(*args, **kwargs)


def informal(cumprimento, título=' '):
    return f'{cumprimento}, {título}'


def extremaFormalidade(cumprimentoHora, nome, sobrenome):
    return f'{cumprimentoHora}, {nome} {sobrenome}'


executando = saudacao(informal, 'olá', 'capitão')
print(executando)
print()
executando2 = saudacao(extremaFormalidade, "bom dia", "William", "Martins")
print(executando2)
