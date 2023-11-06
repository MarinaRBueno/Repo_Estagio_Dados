# %%
"""
*args permite o uso de argumentos puramente posicionais (argumentos sem nome).
**kwargs permite acrescentar argumentos nomeados em função.
"""


def f(*args, **kwargs):
    for parametro in args:
        print(parametro)

    for nome, valor in kwargs.values():
        print(f'{nome} = {valor}')


f(1, 3, 4, 'hello', 'alguma coisa', 20)


# %%
