# %%
# import json para reconhecer
# variávl arquivo recebe json
# usei a função load, para ler o arquivo e retornar o objeto.

import json

arquivo = open('person.json', 'r+')
texto = json.load(arquivo)
print(texto)

# %%
