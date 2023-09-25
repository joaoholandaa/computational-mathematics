def somar(A, B):
  C = []
  #verificar se A e B tem a mesma ordem
  nLinhasA, nLinhasB = len(A), len(B)
  nColA, nColB = len(A[0]), len(B[0])

  if (nLinhasA == nLinhasB) and (nColA == nColB):
    for i in range(nLinhasA):
      linha = [0]*nColA
      C.append(linha)
      for j in range(nColA):
        C[i][j] = A[i][j] + B[i][j]
  else:
    print("Matrizes não tem a mesma ordem")

  return C

def oposta(M):
  O = []
  for i in range(len(M)):
    linha = [0]*len(M[0])
    O.append(linha)
    for j in range(len(M[0])):
      O[i][j] = -M[i][j]
  return O

def subtrair(A, B):
  return somar(A, oposta(B))

def exibir_matriz(matriz):
  for linha in matriz:
    print(linha)

matriz1 = [[1, 6, 9],
           [3, 7, 2],
           [8, -8, 0],
           [-9, 5, 7]]

matriz2 = [[10, 4, 9],
           [-5, -7, 0],
           [0, 2, -12],
           [8, 8, 0]]

exibir_matriz(somar(matriz1, matriz2))
print()
exibir_matriz(subtrair(matriz1, matriz2))