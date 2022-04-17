import json
import os


dicionario = {
    'Pessoa1': {
        'Nome': 'Jao',
        'Idade': 24,
        'Pais': 'bOSTIL'
    },
    'Pessoa2': {
        'Nome': 'Aurora',
        'Idade': 17,
        'Pais': 'Finlandia'
    },
    'Pessoa3': {
        'Nome': 'Carlos Magno',
        'Idade': 1208,
        'Pais': 'Sacro Imperio Romano-Germanico'
    }
}
dicionario_jason = json.dumps(dicionario, indent=True)
with open('12-files/dicionario.json', '+w') as file:
    try:
        file.write(dicionario_jason)
        file.seek(0)
        for linha in file:
            print(linha)
    except Exception as e:
        print(e)
    finally:
        file.close()

apagar = int(input("Digite [3] se deseja apagar, outro número caso não: "))
if apagar == 3:
    os.remove('12-files/dicionario.json')
else:
    print("Ok então")
