# %%
# utilizei o set para retirar elementos repetidos da lista
# utilizei o list para gerar uma nova lista

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
nova_lista = set(lista)
print(list(nova_lista))

# ou

a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(list(set(a)))
