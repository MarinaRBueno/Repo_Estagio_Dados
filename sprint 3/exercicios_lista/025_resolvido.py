# %%


class Aviao:
    w = 'azul'

    def __init__(self, modelo, veloxidade_maxima, capacidade):
        self.x = modelo
        self.y = veloxidade_maxima
        self.z = capacidade


a = []
a.append(Aviao('BOIENG456', 1500, 400))
a.append(Aviao('Embraer Praetor 600', 863, 14))
a.append(Aviao('Antonov An-2', 258, 12))

for caracteristica in a:
    print(f"O avião de modelo {caracteristica.x} possui uma velocidade máxima de {caracteristica.y} km/h, capacidade para {caracteristica.z} passageiros e é da cor {caracteristica.w} ")

# %%
