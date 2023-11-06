# %%
# Utilizei a função open() para abrir o arquivo
# readlines() para exibir todo o conteudo do arquivo
# for para percorrer todas as linhas

arquivo_texto = open('arquivo_texto.txt', 'r+')
texto = arquivo_texto.readlines()
for linha in texto:
    print(f'{linha}', end="")
