estudantes = open('estudantes.csv', 'r+')
# abrindo o arquivo e colocando em uma váriavel
arquivo_estudantes = estudantes.readlines()
# outra variável para leitura de todo  arquivo .csv


def organiza_arquivos(arquivo_estudantes):

    for linha in sorted(arquivo_estudantes):
        info = linha.split(',')
    # split utilizado como separador na virgula
        nome = info[0]
    # nome recebe a posição zero
        notas = list(map(int, info[1:]))
    # notas recebe lista, map percorrendo cada posição
    # a partir da linha 1 e transformando em int
        maiores_notas = sorted(notas, reverse=True)[:3]
    # sorted usado para trazer as notas em ordem decrescente
    # somente as três primeiras notas
        media = round(sum(maiores_notas) / 3, 2)
    # media recebe a soma das 3 notas maiores, dvidido por 3
    # com 2 casas decimais
        print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")


organiza_arquivos(arquivo_estudantes)
