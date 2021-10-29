
### Resolução do problema do caixeiro viajante por meio do uso de Algoritmos Genéticos 

O projeto consiste num algoritmo para a resolução no problema clássico do caixeiro viajante e toda a resolução dele é baseada na técnica de Algoritmos Genéticos que utiliza da teoria da evolução e conceitos genéticos para encontrar o melhor resultado.

---
# ALGORITMOS GENÉTICOS 
Uso de conjunto de métodos heurísticos, os Algoritmos Genéticos se trata de uma meta-heurística que utiliza de fundamentos evolucionistas e genéticos para atingir, com facilidade e pouco custo operacional, uma solução que pode ser considerada razoável. 

# CAIXEIRO VIAJANTE
Problema do Caixeiro Viajante consistem em encontrar a melhor solução que compoe um trajeto visitando **n** cidades e retornando a cidade de origem. Sendo a melhor solução aquela que possuir a menor distância possível ao se cumprir o trajeto com todas as características ditas acima.

## Modelagem    
O problema usa de cromossomos para representar soluções. Dessa maneira os alelos neles presentes representam as cidades passadas pelo trajeto do caixeiro viajante, tendo os únicos valores possíveis de 0 e 1, servindo de um <code>boolean</code>, no qual 1 é um cidade visitada e 0 uma cidade ignorada. 

* **Função Aptidão**

    A função aptidão é responsável por classificar os melhores individuos, ou seja os mais adaptados, que serão escolhidos para a seleção do cruzamento. Para isso elaboramo que a função aptidão é a razão do número de cidades visitas pela distancia total do trajeto.