# %%
"Def primo = função para definir se o numero é primo."


def primo(numero):
    if numero < 2:
        return False
    for posicao in range(2, numero):
        if numero % posicao == 0:
            return False
    return True


for numero in range(1, 101):
    if primo(numero):
        print(numero)
