class Cromossomo:
    aptidao = 0
    genes = list()

    def __init__(self, genes):
        self.genes = genes

    def __call__(self):
        print(self.genes)