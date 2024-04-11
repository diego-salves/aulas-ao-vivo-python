"""
EXERCÍCIOS

1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.34.2.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.34.2.5
85.345.1.2
9.8.234.5
192.168.0.256

A regra é que o intervalo de endereçamento de IP vai de 0.0.0.0 a 255.255.255.255.
"""


def valida_ips(lista_de_ips):
    ips_validos = []
    ips_invalidos = []

    for ip in lista_de_ips:
        intervalo = ip.split('.')
        if len(intervalo) == 4 and all(x.isdigit() and 0 <= int(x) < 256 for x in intervalo):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

    return ips_validos, ips_invalidos


# Lendo a lista de um arquivo .txt
with open('lista_ips.txt', 'r') as f:
    lista_de_ips = f.read().splitlines()

ips_validos, ips_invalidos = valida_ips(lista_de_ips)

# Escrevendo os IPs válidos em um novo arquivo
with open('ips_validos.txt', 'w') as f:
    for ip in ips_validos:
        f.write(ip + '\n')

# Escrevendo os IPs inválidos em um novo arquivo
with open('ips_invalidos.txt', 'w') as f:
    for ip in ips_invalidos:
        f.write(ip + '\n')
