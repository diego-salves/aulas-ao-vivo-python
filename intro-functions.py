# função

"""
Função é um bloco de código, que só é executado quando é chamado.
Utilizado para reutilização de código.

Syntax =

def minha_funcao():
    bloco1
"""


def mensagem():
    print("Olá")


# chamando a função
mensagem()

produtos = {
    'arroz': 5.99,
    'feijão': 3.50,
    'macarrão': 2.99,
    'óleo de soja': 4.50,
    'leite': 2.79,
    'ovos': 3.99,
    'carne moída': 12.50,
    'frango inteiro': 8.99,
    'batata': 2.49,
    'cebola': 1.99,
    'alface': 1.50,
    'tomate': 2.00,
    'banana': 1.29,
    'maçã': 2.99,
    'cenoura': 1.79,
    'sabonete': 1.99,
    'shampoo': 4.50,
    'pasta de dente': 2.29,
    'detergente': 1.99,
    'sabão em pó': 5.99
}


# num mercado, precisamos criar uma função que adiciona 2% de juros a uma lista de valores.

#valores = (valores / 100) * 102    - forma não recomendada
#valores *= 1.02 - forma recomendada

def aumenta2por_cento(valores):
    """
    :param valores: valor do produto a ser aumentado em 2 por cento
    :return: retorna o valor do produto após o acréscimo
    """

    for cont in valores:
        result = round(valores[cont] * 1.02, 2)
        valores.update({cont: result})
    return valores


aumenta2por_cento(produtos)

print(produtos)

produtos_novos = {
    'pão': 2.49,
    'leite condensado': 3.99,
    'café': 6.50,
    'queijo muçarela': 9.99,
    'presunto': 7.50,
    'iogurte': 2.79,
    'batata doce': 3.49,
    'espinafre': 2.00,
    'abacaxi': 3.29,
    'limão': 1.79,
    'papel higiênico': 6.99,
    'detergente para louça': 2.50,
    'amaciante de roupas': 8.99,
    'sabonete líquido': 3.29,
    'sabão em barra': 1.99,
    'escova de dentes': 1.49,
    'creme dental': 2.99,
    'desodorante': 4.50,
    'shampoo anti-caspa': 5.50,
    'condicionador': 4.50,
    'cereal matinal': 4.99
}

aumenta2por_cento(produtos_novos)

print(produtos_novos)
