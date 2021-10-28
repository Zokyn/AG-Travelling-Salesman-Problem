from random import randint
# from populacao import Populacao
class Natureza:
    tamanho_cromossomo = 0 
    tamanho_populacao = 0
    # populacao_cromossomo : Populacao

    def __init__(self, tamanho_cromossomo, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.tamanho_cromossomo = tamanho_cromossomo
        # self.populacao_cromossomo = Populacao(self.tamanho_populacao, tamanho_cromossomo)

    @staticmethod
    def gerarGenes(tamanho_do_cromossomo):
        n = tamanho_do_cromossomo

        genes = list()
        for i in range(n):
            genes.append(randint(0, 1))
        
        return genes


