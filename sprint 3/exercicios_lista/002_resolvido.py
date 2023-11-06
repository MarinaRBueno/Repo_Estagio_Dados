# %%
"""Se o resto da divisão do numero por 2 for igual a 0, então o numero é par.
Se não o numero é impar"""

for posicao in range(3):
    numero = int(input())
    if numero % 2 == 0:
        print(f"Par: {numero}")

    else:
        print(f"Ímpar: {numero}")
