# %%

class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self,):
        self.ordemC = sorted(self.listaBaguncada)
        return self.ordemC

    def ordenacaoDecrescente(self):
        self.ordemD = sorted(self.listaBaguncada, reverse=True)
        return self.ordemD


crescente = Ordenadora([3,4,2,1,5])
z = crescente.ordenacaoCrescente()
print(z)
descrecente = Ordenadora([9,7,6,8])
y = descrecente.ordenacaoDecrescente()
print(y)

# %%
