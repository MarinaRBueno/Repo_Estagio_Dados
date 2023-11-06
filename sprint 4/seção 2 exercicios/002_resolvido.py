""" A função filter é aplicada na string de entrada e utilizando o lambda\
    podemos verificar se a letra (em minuscula, lower()) está presente em\
    vogais. O resultado é convertido em lista e a quantidade de vogais é\
        contada pela função len."""


def conta_vogais(texto: str) -> int:
    x = texto
# o texto recebido é armazenado na variável x
    vogais = "aeiou"
# vogais recebe a string "aeiou"
    solucao = len(list(filter(lambda letra: letra.lower() in vogais, x)))
    return solucao
