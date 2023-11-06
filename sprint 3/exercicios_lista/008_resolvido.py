# %%
"""
Utilizei o -1 para inverter a palavra e comparar com o formato\
original, detectando se é palíndromo ou não. Usei [] para percorrer\
    cada posição da lista.
"""

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
if str(lista[0]) == str(lista[0])[::-1]:
    print("A palavra:", lista[0], "é um palíndromo")
else:
    print("A palavra:", lista[0], "não é um palíndromo")

if str(lista[1]) == str(lista[1])[::-1]:
    print("A palavra:", lista[1], "é um palíndromo")
else:
    print("A palavra:", lista[1], "não é um palíndromo")

if str(lista[2]) == str(lista[2])[::-1]:
    print("A palavra:", lista[2], "é um palíndromo")
else:
    print("A palavra:", lista[2], "não é um palíndromo")

if str(lista[3]) == str(lista[3])[::-1]:
    print("A palavra:", lista[3], "é um palíndromo")
else:
    print("A palavra:", lista[3], "não é um palíndromo")

if str(lista[4]) == str(lista[4])[::-1]:
    print("A palavra:", lista[4], "é um palíndromo")
else:
    print("A palavra:", lista[4], "não é um palíndromo")

if str(lista[5]) == str(lista[5])[::-1]:
    print("A palavra:", lista[5], "é um palíndromo")
else:
    print("A palavra:", lista[5], "não é um palíndromo")
