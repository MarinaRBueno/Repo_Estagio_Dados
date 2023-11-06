# %%
"""
# map() para aplicar a função em cada item da lista.
# lambda() para elevar a base para a segunda potência.
# pow()  para calcular potências inteiras exatas.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_map = list(map(lambda x: x ** 2, lista))
print(f'{list(my_map)}')

"Os dois códigos dão certo."

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
base = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
my_map = list(map(pow, lista, base))
print(f'{my_map}')
