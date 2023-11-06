# %%

class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma1(self):
        soma1 = self.x + self.y
        return str(soma1)

    def subtracao(self):
        subtracao = self.x - self.y
        return str(subtracao)

    def subtracao_com_negativos(self):
        numero_negativo = self.x + self.y
        return str(numero_negativo)


numeros = Calculo(4, 5)
somando = numeros.soma1()
numeros = Calculo(4, 5)
subtraindo = numeros.subtracao()
numeros = Calculo(4, -5)
subtraindo_negativos = numeros.subtracao_com_negativos()
print("Somando: ", somando)
print("Subtraindo: ", subtraindo)
print("Subtraindo: ", subtraindo_negativos)
