breakfast = {
    "proteina": "ovo",
    "carboidrato": "pão",
    "gordura": "manteiga"
}
almoço = {"proteina": "carne",
          "carboidrato": "arroz e feijão",
          "gordura": "carne"}
janta = {"proteina": "frango",
         "carboidrato": "nenhum",
         "gordura": "frango"}

refeicoes = [breakfast, almoço, janta]
print(refeicoes[1]["proteina"])
print(refeicoes)
print()
# tuplas dentro de dicinoarios
dicionarioTupla = {
    'nome': 'carlão',
    'idade': 14,
    'salario da mae': 1400,
    'localizacao': (34.243, -23434)
}
print(dicionarioTupla['localizacao'])
