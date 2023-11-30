import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')

# Set/ dict comprehension

# {chave: valor for elemento in iteravel}

dicionario = {elemento: elemento*2 for elemento in range(6)}

print(dicionario)

lista = ['Ferrari', 'Lamborghini', 'Porsche']
dicionario = {
    f'{elemento.lower()}': f'Montadora: {elemento.upper()}' for elemento in lista
}

print(dicionario)

print('-'*20)

carros_esportivos = {
    'ferrari': 1299000,
    'lamborghini': 1100000,
    'porsche': 800000
}

dict_saida = {
    chave: f'{chave.upper()} : {locale.currency(valor)}' for chave, valor in carros_esportivos.items()
}

print(dict_saida)

# Usando IF/Else
# {chave if condicao: valor for elemento in iteravel}
# {chave: valor if condicao for elemento in iteravel}
# {chave: expressao for elemento in iteravel if condicao}


carros_esportivos = {
    'ferrari': 1299000,
    'lamborghini': 1100000,
    'porsche': 800000
}

dict_saida = {
    chave: f'{chave.upper()} : {locale.currency(valor)}'
    for chave, valor in carros_esportivos.items() if valor > 1000000
}

print(dict_saida)

carros_esportivos = {
    'ferrari': 1299000,
    'lamborghini': 1100000,
    'porsche': 800000
}

dict_saida = {
    chave if valor > 1000000 else f'{chave}-valor-abaixo':
    f'{chave.upper()} : {locale.currency(valor)}'
    if valor > 1000000 else f'{chave.upper()}: Valor abaixo de R$ 1.000.000,00'
    for chave, valor in carros_esportivos.items()
}

print(dict_saida)