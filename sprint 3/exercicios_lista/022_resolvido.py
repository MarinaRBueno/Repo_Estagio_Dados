# %%

class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ""

    def nome(self, nome):
        self.__nome = nome
        return self.__nome


pessoa = Pessoa(0)
pessoa.nome = ('Fulano De Tal')
print(pessoa.nome)

# %%
