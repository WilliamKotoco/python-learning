# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velo = (input("digite a velociade do carro: "))
if velo:
    velo = int(velo)
    if velo < 80:
        print("Nenhum problema relatado")
    else:
        limite = velo - 80
        print("Você foi multado por {} reais".format(limite))
else:
    print("Digite um valor")
