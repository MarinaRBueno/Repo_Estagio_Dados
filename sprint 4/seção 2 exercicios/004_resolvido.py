"""Dicionário utilizado para compilar as funções com o lambda\
depois de cada operação em seu lugar, variável valores recebe uma lista\
com função map e um lambda declarando a ordem dos operadores e operandos\
desempacotando a tupla contida na lista de operandos."""


def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda c, d: c - d,
        '*': lambda e, f: e * f,
        '/': lambda g, h: g / h,
        '%': lambda i, j: i % j,
    }

    valores = list(map(lambda x: operacoes[x[0]](*x[1]), zip(operadores, operandos)))
    return max(valores)


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)
