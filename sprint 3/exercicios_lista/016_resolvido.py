# %%
"""função usada para retirar elementos de uma string e retornar
a soma de todos os numeros inteiros."""


def funcao_soma(numeros_num):
    numero = numeros_num.split(',')
    soma = 0
    for posicao in numero:
        soma += int(posicao)
    return soma


somafinal = funcao_soma('1,3,4,6,10,76')
print(somafinal)


# %%
