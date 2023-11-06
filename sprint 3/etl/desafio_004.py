# %%
"""
Trabalhei com dicionário para contar a repetição dos filmes e mostrar\
o valor, depois trouxe o mais repetido.
"""
arquivo_atores = open('actors.csv', 'r+')
linhas_do_arquivo = arquivo_atores.readlines()

nome_filme = []
filmes_repetidos = {}


def get_filmes_com_maior_frequencia():
    for filme in nome_filme:
        if nome_filme.count(filme) > 1:
            filmes_repetidos[filme] = nome_filme.count(filme)

    if filmes_repetidos:
        print('Filmes repetidos:')
        for filme, i in filmes_repetidos.items():
            print(f'{filme}: {i}')
        print(f"Filme com maior frequência: {max(filmes_repetidos, key=filmes_repetidos.get)}")


for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    nome_filme.append(colunas[4])

get_filmes_com_maior_frequencia()

arquivo_atores.close()
