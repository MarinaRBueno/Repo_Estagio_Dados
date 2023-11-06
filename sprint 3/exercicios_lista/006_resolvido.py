# %%

"""O primeiro código percorre as duas listas comparando cada elemento\
detectando os elementos iguais.
Utilizei o conceito de conjuntos, aplicando a intersecção\
trazendo os numeros repetidos nas duas listas.
"""

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numeros_repetidos = [elemento for elemento in a if elemento in b]
print(list(set(numeros_repetidos)))


a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numeros_repetidos = (set(a) & set(b))
print(list(numeros_repetidos))
