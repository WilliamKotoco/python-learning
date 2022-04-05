# String são importantes para organizar informações, textos, etc
# Strings são sequências de caracteres, sendo cada caracter um índice
nome = "william"
print(nome[0])  # zero é sempre o primeiro valor

# primeiro valor de trás pra frente (também conhecido como último)
print(nome[-1])

print(nome[:3])  # Pega todo o texto e para no índice 3
# pega do caractere 3 e vai até o caractere 5 (ou ate o final, caso deixe vazio)
print(nome[3:5])


# função para verificar o tamanho de uma stringer
size = len(nome)
print(size)
print()
print(nome[-6])
