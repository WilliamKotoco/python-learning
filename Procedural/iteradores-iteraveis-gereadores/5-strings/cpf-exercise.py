# Faça um cadastro de CPF com as validações necessárias
cpf = input("Digite seu CPF (digite apenas números): ")
cpf = cpf.strip()

if cpf.isnumeric():
    if len(cpf) == 11:
        print("Cpf válido")
    else:
        print('CPF inválido! Precisa de 11 números')
else:
    print('Só pode ter número no CPF')
