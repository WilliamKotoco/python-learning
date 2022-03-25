'''
:s - texto(strings)
:d - Inteiros (int)
:f - float, decimais
:.(número)f - quantidade de casas decimais
:(caractere) (> ou <) (quantidade) (tipo -s, d ou f)
'''
divisão = 10/3
print(f'{divisão: .2f}')  # ou print("{:.2f}".format(divisão) )
print()
nome = "william"
nome_formatado = '{:$^30}'.format(nome)
num1 = 158
num2 = 30
num3 = 96
print(f'{num1:0>10}')
print(f'{num2:0^10}')
print(f'{num3:0<10}')
print()
print(f'{nome_formatado}')
