email = input("Digite seu email: ")
if email:
    if email.find("@") and email.find(".") == -1:
        # quando o método .find não encontra, ele retorna -1
        print("Email válido!")
    else:
        pass
else:
    print('Preencha seu e-mail')
