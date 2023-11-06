"""Função calcular_valor feita para receber um parâmetro chamado\
    lançamento, ele separa a lista como valor e tipo e se o tipo\
    for = 'C' então subtrai o valor do acumulador que está\
    na próxima função, calcula_saldo que recebe a lista\
    lancamentos, e possui a variável valores com o map\
    e a função calcular_valor com lancamentos como parametro\
    variável saldo recebe reduce com acumulador em zero, e\
    lambda passando os parametros acumulador e valor fazendo a\
    soma, basicamente assim que as funções são executadas, se\
    o tipo for 'C' então subtrai o valor, e se for 'D' soma o\
    valor no acumulador."""


from functools import reduce


def calcular_valor(lancamento):
    valor, tipo = lancamento
    return valor if tipo == 'C' else - valor


def calcula_saldo(lancamentos):
    valores = map(calcular_valor, lancamentos)
    saldo = reduce(lambda acumulador, valor: acumulador + valor, valores, 0)
    return saldo


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

saldo_final = calcula_saldo(lancamentos)
print(saldo_final)
