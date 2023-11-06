
# %%

class Passaro:

    def __init__(self, nome):
        self.nome = nome

    def especie_passaro(self):
        return f'{self.nome}'


class Pato(Passaro):

    def __init__(self, nome):
        super().__init__(nome)

    def especie_passaro(self):
        return super().especie_passaro()

    def pato_voando(self):
        print('Voando...')

    def tipo_som(self):
        print('Pato emitindo som...')
        print('Quack Quack')


class Pardal(Passaro):

    def __init__(self, nome):
        super().__init__(nome)

    def especie_passaro(self):
        return super().especie_passaro()

    def pardal_voando(self):
        print('Voando...')

    def tipo_som(self):
        print('Pardal emitindo som...')
        print('Piu Piu')


pato = Pato('Pato')
print(pato.especie_passaro())
pato.pato_voando()
pato.tipo_som()

pardal = Pardal('Pardal')
print(pardal.especie_passaro())
pardal.pardal_voando()
pardal.tipo_som()
