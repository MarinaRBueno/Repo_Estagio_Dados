# %%

"""Como se tratava de um arquivo csv, achei melhor trabalhar com colunas\
eliminando o cabeçalho para não atrapalhar os números.
Fiz um for percorrendo as linhas do arquivo e onde o separador ","\
estava, ordenei para se formar colunas de 0 a N-1, ou seja 0 a 5.
Com as colunas prontas e cabeçalho deletado, ficou mais fácil trabalhar\
com os números. Onde tinha o separador " ", usei o replace\
para substituir a formatação por uma ordem correta.
Em breve estudarei uma forma para automatizar, a correção de\
inumeros erros encontrados em arquivos. Onde foi necessário\
    voltei o cabeçalho."""

# Abri o arquivo e percorri todo o conteudo.
arquivo_atores = open('actors.csv', 'r+')
linhas_do_arquivo = arquivo_atores.readlines()

'variáveis para receber as colunas.'
atores = []
total_bruto = []
quantidade_filmes = []
media_por_filme = []
nome_filme = []
bruto = []

# As funções dos exercícios.

# Montei as colunas com essa base.
for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    atores.append(colunas[0])
    total_bruto.append(colunas[1])
    quantidade_filmes.append(colunas[2])
    media_por_filme.append(colunas[3])
    nome_filme.append(colunas[4])
    bruto.append(colunas[5])

arquivo_atores.close()
