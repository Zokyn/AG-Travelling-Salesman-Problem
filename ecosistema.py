from random import randint

class Natureza:

    @staticmethod
    def gerarGenes(tamanho_do_cromossomo):
        n = tamanho_do_cromossomo

        genes = list()
        for i in range(n):
            genes.append(randint(0, 1))
        
        return genes