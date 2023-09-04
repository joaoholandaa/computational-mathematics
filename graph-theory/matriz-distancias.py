class Grafo:
    
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0]*self.vertices for i in range(self.vertices)]

  def adcionar_aresta(self, u, v, peso):
    #grafos direcionados simples
    self.grafo[u-1][v-1] = peso
    #trocar = por += se for grafo múltiplo
    #self.grafo[v-1][u-1] = 1 se o grafo não for direcionado

  def mostra_matriz(self):
    print("A matriz de distâncias é:")
    for i in range(self.vertices):
      print(self.grafo[i])

v = int(input("Digite a quantidade de vértices? "))
g = Grafo(v)

a = int(input("Digite a quantidade de arestas? "))
for i in range(a):
  u = int(input("De qual vértice parte esta aresta? "))
  v = int(input("Para qual vértice vai esta aresta? "))
  p = int(input("Qual é o peso desta aresta? "))
  g.adcionar_aresta(u, v, p)

g.mostra_matriz()