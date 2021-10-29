from cromossomo import Cromossomo
from ecosistema import Natureza
from caixeiro import Caixeiro
# from populacao import Populacao
# from cidade import Cidade

### TESTES
# new = Caixeiro(4)
# cidadeA = new.cidades[0]
# cidadeB = new.cidades[1]

# cidadeA(), cidadeB()
# distancia = cidadeA.distancia(cidadeB)
# print('A distancia AB é: {:0.3f} km'.format(distancia))

# new = Cromossomo(Natureza.gerarGenes(10))
# new()

n = 6
new = Cromossomo(Natureza.gerarGenes(n))
a = Caixeiro()
a.recebeCidades()

print('CIDADES:')
a()
print('Cromossomo 1')
new()

aptidao = a.funcao_aptidao(new)
print(f'Aptidao do Cromossomo: {aptidao}')