# %%
# Utilizei o .append para adicionar os numeros impares na lista vazia.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_impar = []

for numero in a:
    if numero % 2 != 0:
        lista_impar.append(numero)

print(lista_impar)
