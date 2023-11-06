# %%


class Lampada:

    def __init__(self, estado_lampada=False, ligada=False):
        self.estado_lampada = estado_lampada
        self.ligada = ligada

    def liga(self):
        self.estado_lampada = True

    def desliga(self):
        self.estado_lampada = False

    def esta_ligada(self):
        return self.estado_lampada


y_liga = Lampada()
y2 = y_liga.liga()
print('A lampada esta ligada?', y_liga.esta_ligada())

x_desliga = Lampada()
x2 = x_desliga.desliga()
print('A lampada ainda continua ligada?', x_desliga.esta_ligada())
