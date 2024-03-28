# *args (arbitrary arguments)

def somar(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(somar(1, 2, 3, 4))


# ** kwargs (arbitrary keyword arguments)

def testando_kwargs(**dados):
    print(f"O seu último nome é " + dados["last_name"] + " e o seu primeiro é " + dados["first_name"]
          + " e vc tem " + dados["age"] + " anos.")


testando_kwargs(first_name="Diego", last_name="Alves", age="27")
