# Write an if statement that asks for the user's name via input() function.
# If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print
# "Good morning NAME". (Replace Name with user's name)
name = input("Qual é teu nome ?")
if name:
    if (name == "Bond" or name == "bond"):
        print("Bem vindo a bordo, 007")
    else:
        print("Bom dia {}".format(name))
else:
    print("Preencha seu nome, paspalho!")
