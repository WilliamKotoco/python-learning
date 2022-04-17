# cria um jogo da forca
letrasTentadas = []
listaCaracteresPalavra = []
palavra = input("Digite uma palavra: ")
for i in palavra:
    listaCaracteresPalavra.append("_")
for i in range(10, 0, -1):
    print(i)
print("Agora dê o computador para outra pessoa")

tentativas = 0
while tentativas < 5:
    letra = input("Digite uma letra: ")
    letrasTentadas.append(letra)
    if letra in palavra:
        print("A letra existe")
    else:
        tentativas += 1
        letrasTentadas.pop()
        print(f"Ainda restam {5 - tentativas} tentativas")
    palavraFormada = ''
    for letraAdvinhada in palavra:
        if letraAdvinhada in letrasTentadas:
            palavraFormada += letraAdvinhada
        else:
            palavraFormada += ' _ '
    print(palavraFormada)
    if palavraFormada == palavra:
        print("Parabéns, você ganhou")
        break

else:
    print("Tentativas esgotadas")
    print("a palavra era {}".format(palavra))
