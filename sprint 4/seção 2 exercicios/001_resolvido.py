lista = open('number.txt', 'r+')
# variavel lista recebe o arquivo texto em modo leitura
lista_de_numeros = lista.readlines()

valor_maximo = sorted(filter(lambda x: x % 2 == 0, map(int, lista_de_numeros)), reverse=True)[:5]
# valor_maximo recebe a lista com função sorted reverse true
# função lambda trazendo os números pares com o\
#  map percorrendo lista_de_numero
# limite de 5 valores máximos
print(valor_maximo)
print(sum(valor_maximo))
