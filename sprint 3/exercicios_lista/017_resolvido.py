# %%


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
contagem_numeros = len(lista)
divisao_lista = contagem_numeros // 3
lista_1 = lista[:divisao_lista]
lista_2 = lista[divisao_lista:2*divisao_lista]
lista_3 = lista[2*divisao_lista:]

print(lista_1, lista_2, lista_3)
