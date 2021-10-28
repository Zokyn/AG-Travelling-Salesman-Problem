from cromossomo import Cromossomo
from ecosistema import Natureza
class Populacao:
    tamanho_da_populacao = 0
    
    lista_de_cromossomos = list()
    lista_de_genes = list()
    lista_de_aptidoes = list()

    def adicionar_cromossomo(self, cromossomo):
        self.lista_de_cromossomos.append(cromossomo)

    def __init__(self, tamanho_populacao, tamanho_locus):
        
        self.tamanho_da_populacao = tamanho_populacao
        # Preenche a lista de cromossomos
        self.lista_de_cromossomos = list()
        for i in range(tamanho_populacao):
            individuo = Cromossomo(Natureza.gerarGenes(tamanho_locus))
            self.lista_de_cromossomos.append(individuo)

        cromossomos = self.lista_de_cromossomos
        
        # Preenche a lista de genes
        self.lista_de_genes = list()
        for cromossomo in cromossomos:
            gene = cromossomo.genes
            self.lista_de_genes.append(gene)

        # Preenche a lista de aptidoes
    def __call__(self):
        populacao = self.lista_de_cromossomos
        for individuo in populacao:
            individuo()