def convertenumero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass    # returna none por padrão


numero = convertenumero(input("Digite um número: "))

if numero is not None:
    print(numero)
else:
    print('Não é um número')
