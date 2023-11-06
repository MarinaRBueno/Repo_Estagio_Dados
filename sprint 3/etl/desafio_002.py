# %%
"""
Como o arquivo já trazia a média por filmes, associei isso a coluna\
ator, ou seja, o valor médio por filme associado a autor.
"""
arquivo_atores = open('actors.csv', 'r+')
linhas_do_arquivo = arquivo_atores.readlines()

atores = []
media_por_filme = []


def get_media_por_bruta_ator():
    for ator, quantidade in zip(atores[1:], media_por_filme[1:]):
        print(f'A média de faturamento por Ator/Atriz é de: {ator}, {quantidade}')


for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    atores.append(colunas[0])
    media_por_filme.append(colunas[3])


get_media_por_bruta_ator()

arquivo_atores.close()
