# %%
"""O arquivo já trazia o conceito de ordem decrescente\
    então, somente organizei cada um em sua posição."""

arquivo_atores = open('actors.csv', 'r')
linhas_do_arquivo = arquivo_atores.readlines()

atores = []
total_bruto = []


def get_total_bruto_ordenado():
    for ator, total in zip(atores[1:], total_bruto[1:]):
        print(f'{ator}: {total}')


for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    atores.append(colunas[0])
    total_bruto.append(colunas[1])


get_total_bruto_ordenado()

arquivo_atores.close()

# %%
