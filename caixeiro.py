import random
import string
from cidade import Cidade
CIDADES = [ [3.68, 6.54], [9.68, -2.49], [-7.93, 1.73],
            [0.94, 3.04], [2.65, -5.35], [1.1, 9.83] ]
NOMES = list(string.ascii_uppercase)
AREA = [-10.0, 10.0]

class Caixeiro: 
    # Classe problema que recebe os parametros para que 
    # seja solucionado. Com isso temos, uma lista de cidade
    # e um trajeto a ser elaborado por meio da solução (cromossomo)
    # ela que definirá o valor da aptidao de um individuo, ou
    # seja de um solução possível.
    cidades = list()
    def recebeCidades(self):
        cidades = list(); i = 0
        for i in range(len(CIDADES)):
            coord = CIDADES[i]
            new = Cidade(i, coord[0], coord[1])

            self.cidades.append(new)
    # Gerando cidades aleatórias
    def gerarCidades(self, quantidade):
        # Se o numero de cidades for menor ou igual
        # ao numero de letras no alfabeto, podemos 
        # usa-las como base para nomear cidades
        i = 0
        if quantidade <= 26:
            # Gera a quantidade de cidades dada
            for i in range(quantidade):
                n = NOMES[i] # atribui o nome a ela
                
                # cria coordenadas aleatorias dentro da 
                # area onde deveram se encontrar todas cidades
                x = random.uniform(min(AREA), max(AREA))
                y = random.uniform(min(AREA), max(AREA))

                nova_cidade = Cidade(n, x, y)
                self.cidades.append(nova_cidade)
        # Caso contrário, serão mais cidades do que
        # somos capazes de nomear, portanto usaremos
        # simplesmente numeros para identifica-las
        else:
            for i in range(quantidade):
                    n = i+1
                    
    #                 x = random.uniform(-10.0, 10.0)
    #                 y = random.uniform(-10.0, 10.0)

    #                 nova_cidade = Cidade(n, x, y)
    #                 self.cidades.append(nova_cidade)
    
    # Atribuindo aptidao ao cromossomo         
    def funcao_aptidao(self, cromossomo): 
        # A função aptidão é dada pela distancia euclidiana do trajeto
        # Sendo genes o conjunto de variaveis que forma uma solução
        solucao = cromossomo.genes 

        ## DEFININDO TRAJETO
        # Geramos o trajeto baseado na solução
        trajeto = list() 
        # Contadora de loop e contadora de cidades
        percorridas = 0; i = 0
        # Para cada variavel, ou alelo
        for variavel in solucao:
            if variavel == 1:
                # Temos uma cidade no trajeto
                trajeto.append(self.cidades[i])
                # Acrescentamos o numero de cidades
                percorridas += 1
            i += 1
        # Se houver apenas uma ou nenhum cidade no trajeto então
        # devemos descartar a solução, para isso atribuimos sua 
        # aptidao a zero, para que os operadores evitem que esse
        # cromossomo perpetue suas caracteristicas na população
        if(len(trajeto) <= 1):
            aptidao = 0
        else: 
            # Agora que sabemos o trajeto pecorrido pela solução
            aptidao = 0 # podemos achar a aptidao da solução por
            soma_distancias = 0 # meio da soma das distancias das
            # Variaveis auxiliar
            cidade_anterior = None # cidades presentes no trajeto
            cidade_inicial = None
            ## DEFININDO APTIDAO
            # Para cada cidade do trajeto
            for cidade in trajeto:
                if(cidade_anterior):
                    # comparamos a distancia dela com a cidade anterior
                    distancia = cidade.distancia(cidade_anterior) 
                    # E somamos essa distancia com a distancia total
                    soma_distancias += distancia 
                else:
                    cidade_inicial = cidade
                cidade_anterior = cidade # atualizamos a cidade anterior
            # acrescentamos ao trajeto o percurso até a cidade inicial
            distancia = cidade.distancia(cidade_inicial)
            soma_distancias += distancia 
            print('N- de Cidades: ', percorridas)
            print('Distancia: ', soma_distancias)
            # aptidao do cromossomo, é dada pela razão do numero de
            # cidades presentes no trajeto pela soma das distancias 
            # presentes no trajeto dado pela solução (cromossomo)
            aptidao = percorridas/soma_distancias
        
        return aptidao
    # funções build-in
    # def __init__(self, quantidade_de_cidades):
    #     self.gerarCidades(quantidade_de_cidades)

    def __call__(self):
        lista_de_cidade = self.cidades
        for cidade in lista_de_cidade:
            cidade()
