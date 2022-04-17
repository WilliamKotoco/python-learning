# Digite certa quantidade de números e determine quantos e quais sao primos
def VerificacaoPrimo(num):
    contador = 0
    isPrime = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
        else:
            pass
        if contador == 2:
            isPrime = 1
        else:
            isPrime = 0
    return isPrime


quantidade = int(input("Digite a quantidade de números: "))
acumulador = 0
numerosPrimos = []
for i in range(quantidade):
    num = int(input("Digite o número: "))
    if VerificacaoPrimo(num) == 1:
        acumulador += 1
        numerosPrimos.append(num)
    else:
        pass
print("Há {} números primos, que são {}.".format(acumulador, numerosPrimos))
