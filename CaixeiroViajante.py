import random
import string
# cidades = {3.0, 5.5, 6.7, 3.2, 4.2, 1.2, 3.3, 4.2, 5.0}
NOMES = list(string.ascii_uppercase)
AREA = [-10.0, 10.0]
class Cidade:
    # Atributos de uma cidade
    nome = '' 
    coord = [0.0, 0.0] 
    x = 0; y = 0 

    # Função para calular a distancia até outra cidade
    def distancia(self, cidade):
        # distX = pow(abs(cidade.x - self.x), 2)
        # distY = pow(abs(cidade.y - self.y), 2)  

        # Quadrado da distancia de self até cidade  
        distanciaX = pow(cidade.x - self.x, 2)
        # Quadrado da distancia de self até cidade B
        distanciaY = pow(cidade.y - self.y, 2)
        # Distancia Euclidiana é dada pela raiz da soma 
        # do quadrado dos eixos da distancia da cidade 
        distanciaE = pow(distanciaX + distanciaY, 0.5)

        return distanciaE
    def atribuirCoordenadas(self, x, y):
        self.x = x
        self.y = y
        self.coord = [x,y]
    def __init__(self, nomeCidade, x, y):
        x = round(x, 2)
        y = round(y, 2)

        self.nome = nomeCidade
        self.atribuirCoordenadas(x,y)
    def __call__(self):
        print(f'{self.nome}:{self.coord}')

class Caixeiro: 
    # Classe problema que recebe os parametros para que 
    # seja solucionado. Com isso temos, uma lista de cidade
    # e um trajeto a ser elaborado por meio da solução (cromossomo)
    # ela que definirá o valor da aptidao de um individuo, ou
    # seja de um solução possível.
    cidade_inicial = None
    cidades = list()

    # trajeto = list()


    def cidade_inicial(self, cidade):
        self.cidade_inicial = cidade

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
                    
                    x = random.uniform(-10.0, 10.0)
                    y = random.uniform(-10.0, 10.0)

                    nova_cidade = Cidade(n, x, y)
                    self.cidades.append(nova_cidade)
    
    # Atribuindo aptidao ao cromossomo         
    def funcao_aptidao(self, cromossomo):
        # Sendo genes o conjunto de variaveis que forma uma solução
        solucao = cromossomo.genes

        ## DEFININDO TRAJETO
        # Geramos o trajeto baseado na solução
        trajeto = list(); i = 0
        # Para cada variavel, ou alelo
        for variavel in solucao:
            if variavel == 1:
                # Temos uma cidade no trajeto
                trajeto.append(self.cidades[i])
            i += 1

        # Agora que sabemos o trajeto pecorrido pela solução
        aptidao = 0 # podemos achar a aptidao da solução por
        soma_distancias = 0 # meio da soma das distancias das
        cidade_anterior = None # cidades presentes no trajeto
        
        ## DEFININDO APTIDAO
        # Para cada cidade do trajeto
        for cidade in trajeto:
            if(cidade_anterior):
                # comparamos a distancia dela com a cidade anterior
                distancia = cidade.distancia(cidade_anterior) 
                # E somamos essa distancia com a distancia total
                soma_distancias += distancia 
            cidade_anterior = cidade # atualizamos a cidade anterior
        # aptidao do cromossomo, por enquanto, é dada pela soma da  
        # distancia das cidades presentes no trajeto dado pelo 
        # cromossomo
        aptidao = soma_distancias
        return aptidao
    # funções build-in
    def __init__(self, quantidade_de_cidades):
        self.gerarCidades(quantidade_de_cidades)

    def __call__(self):
        lista_de_cidade = self.cidades
        for cidade in lista_de_cidade:
            cidade()
