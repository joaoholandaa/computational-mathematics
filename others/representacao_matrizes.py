def exibir_matriz(matriz):
  for linha in matriz:
    print(linha)

m = int(input("Número de linhas: "))
n = int(input("Número de colunas: "))

matriz = []

for i in range(m):
  linha = []
  for j in range(n):
    elemento = input("Elemento da linha {} e coluna {}: ".format(i, j))
    linha.append(float(elemento))
  matriz.append(linha)

exibir_matriz(matriz)