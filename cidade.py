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
