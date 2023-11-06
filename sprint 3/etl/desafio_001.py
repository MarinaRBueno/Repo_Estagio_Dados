# %%
arquivo_atores = open('actors.csv', 'r+')
linhas_do_arquivo = arquivo_atores.readlines()

atores = []
quantidade_filmes = []


def ator_com_maior_quantidade_de_filmes(filmes):
    filmes = filmes[1:]
    maximo_filmes = max(filmes)
    indice_filme = filmes.index(maximo_filmes)
    nome_ator = atores[indice_filme + 1]
    print(f'O(a) Ator/Atriz com maior quantidade de filmes é: {nome_ator} com {maximo_filmes} filmes.')


for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    atores.append(colunas[0])
    quantidade_filmes.append(colunas[2])

ator_com_maior_quantidade_de_filmes(quantidade_filmes)

arquivo_atores.close()
# %%
