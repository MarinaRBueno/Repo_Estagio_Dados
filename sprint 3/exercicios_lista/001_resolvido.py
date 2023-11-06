# %%

from datetime import date

data = date.today()
nome = str(input('Nome: '))
idade = int(input('Idade: '))
diferenca_idade = 100 - idade
print(f'{data.year + diferenca_idade}')
# váriavel data formatada somente com o ano + diferença das idades.
