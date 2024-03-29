class Grafo:
    
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0]*self.vertices for i in range(self.vertices)]

  def adcionar_aresta(self, u, v):
    #grafos não direcionados
    self.grafo[u-1][v-1] += 1
    if u != v:
      self.grafo[v-1][u-1] += 1 

  def mostra_matriz(self):
    print("A matriz de adjacências é:")
    for i in range(self.vertices):
      print(self.grafo[i])

  def tem_aresta(self, u, v):
    if self.grafo[u-1][v-1] == 0:
      print(f'Não tem aresta entre os vértices {u} e {v}')
    else:
      print(f'Existe {self.grafo[u-1][v-1]} de arestas entre o vértices {u} e {v}')

  def euleriano(self):
    contador = 0
    for i in range(self.vertices):
      grau = 0
      for j in range(self.vertices):
        if i == j:
          grau = grau + 2 * self.grafo[i][j]
        else:
          grau += self.grafo[i][j]
      if grau % 2 != 0:
        contador += 1
    if contador == 0:
      print('É um grafo euleriano!')
    elif contador == 2:
      print('É um grafo semieuleriano!')
    else:
      print('É grafo não é euleriano ou semieuleriano!')

g = Grafo(4)
g.adcionar_aresta(1,2)
g.adcionar_aresta(3,4)
g.adcionar_aresta(2,3)
g.euleriano()
g.mostra_matriz()