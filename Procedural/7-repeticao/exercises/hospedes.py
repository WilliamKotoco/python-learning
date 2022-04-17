qtdHospedes = int(input("Quantos são os hóspedes ? "))
listaTotalHospedes = []


def VerifyCpf(cpf):
    if cpf.isnumeric() and len(cpf) == 11:
        valid = True
    else:
        valid = False
    return valid


for i in range(qtdHospedes):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cpf = cpf.strip()
    if(VerifyCpf(cpf) == True):
        Hospedes = [nome, cpf]
        listaTotalHospedes.append(Hospedes)
    else:
        print("CPF inválido")
        break
print(listaTotalHospedes)
