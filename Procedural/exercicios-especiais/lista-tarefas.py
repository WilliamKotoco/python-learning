
"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def desfazer(lista, ultimoelemento):
    if not lista:
        print('Lista vazia, nada a desfazer')
    else:
        ultimoelemento.append(lista[-1])
        lista.pop()


def listar(lista):
    print()
    print("Tarefas: ")
    print(lista)
    print()


def refazer(listaTarefas, ultimoElemento):
    if not ultimoElemento:
        print("Nada a refazer")
    else:
        listaTarefas.append(ultimoElemento[-1])


listaTarefas = []
ultimoElemento = []
while True:
    opcoes = input('Digite uma tarefa ou "desfazer", "refazer", "listar": ')

    if opcoes.casefold() == 'desfazer':
        desfazer(listaTarefas, ultimoElemento)
        continue

    elif opcoes.casefold() == 'listar':
        listar(listaTarefas)
        continue

    elif opcoes.casefold() == 'refazer':
        refazer(listaTarefas, ultimoElemento)
        continue
    else:
        listaTarefas.append(opcoes)
    continuar = int(
        input("Digite [1] para fechar o programa, outro valor para continuar: "))
    if continuar == 1:
        break
listar(listaTarefas)
