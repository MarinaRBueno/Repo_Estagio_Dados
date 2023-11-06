# %%
arquivo_atores = open('actors.csv', 'r+')
linhas_do_arquivo = arquivo_atores.readlines()

atores = []
media_por_filme = []


def maior_media_faturamento_filme_por_ator():
    numeros = [float(numero) for numero in media_por_filme[1:]]
    maximo_numero = max(numeros)
    for i, numero in enumerate(numeros):
        if numero == maximo_numero:
            ator = atores[1:]
            indice_filme = ator.index(ator[i])
            print(f'O(a) Ator/Atriz com maior faturamento é: {ator[indice_filme]}, com o valor de: {maximo_numero}.')


for linha in linhas_do_arquivo:
    if '"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ' in linha:
        linha = linha.replace('"Robert Downey, Jr.",3947.30 ,53,74.50 ,The Avengers,623.40 ', 'Robert Downey Jr.,3947.30 ,53,74.50 ,The Avengers,623.40 ')
    colunas = linha.split(',')
    atores.append(colunas[0])
    media_por_filme.append(colunas[3])


maior_media_faturamento_filme_por_ator()

arquivo_atores.close()
