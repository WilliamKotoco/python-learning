DIAL_CODES = [
    (86, 'China'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
codigo_pais = {country: code for code, country in DIAL_CODES}
print(codigo_pais)
print()
outroDicionario = {f'quadrado{x}':x**2 for x in range(10)}
print(outroDicionario)

