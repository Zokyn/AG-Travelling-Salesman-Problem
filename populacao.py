from cromossomo import Cromossomo

class Populacao:
    tamanho_da_populacao = 0
    populacao_de_cromossomos = list()

    def adicionar_cromossomo(self, cromossomo):
        self.populacao_de_cromossomos.append(cromossomo)

    def __init__(self, populacao, locus):
        self.tamanho_da_populacao = populacao
        self.populacao_de_cromossomos = list()
        for i in range(populacao):
            individuo = Cromossomo( None, locus)
            self.populacao_de_cromossomos.append(individuo)

    def __call__(self):
        populacao = self.populacao_de_cromossomos
        for individuo in populacao:
            individuo()