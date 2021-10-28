from ecosistema import Natureza
class Cromossomo:
    tamanho = 0 
    aptidao = 0
    genes = list()

    def __init__(self, genes, tamanho):
        if(genes == None):
            self.genes = Natureza.gerarGenes(tamanho)
        else:
            self.genes = genes
        self.tamanho = tamanho        

    def __call__(self):
        print(self.genes)