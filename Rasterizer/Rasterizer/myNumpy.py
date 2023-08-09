from math import isclose

def matrixMultiplier(matrixA, matrixB):
    # Filas y columnas de cada matriz
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])

    # Verificar si las matrices son multiplicables
    if colsA == rowsB:
        # Crear una matriz vacia para almacenar el resultado
        # El tamano esta dado por el numero de filas de A por columnas de B
        matrixC = [[0 for _ in range(colsB)] for _ in range(rowsA)]
        # Realizar la multiplicacion de matrices
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    # Suma de productos de la i-esima fila de A y la j-esima columna de B
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        return None


def vectorXmatrix(matrix, vector):
    # Tamanos de la matriz y el vector
    rows = len(matrix)
    cols = len(matrix[0])
    size = len(vector)

    # Verificar si la matriz y el vector son multiplicables
    if cols == size:
        # Se crea el vector vacio para almacenar resultados
        newVector = [0 for row in range(rows)]

        # Realizar la multipliacion
        for i in range(rows):
            for j in range(cols):
                newVector[i] += matrix[i][j] * vector[j]
        return newVector
    else:
        return None


def barycentrinCoords(A, B, C, P):
    
    # Se saca el area de los subtriangulos y del triangulo
    # mayor usando el Shoelace Theorem, una formula que permite
    # sacar el area de un poligono de cualquier cantidad de vertices.

    areaPCB = abs((P[0]*C[1] + C[0]*B[1] + B[0]*P[1]) - 
                  (P[1]*C[0] + C[1]*B[0] + B[1]*P[0]))

    areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))

    areaABP = abs((A[0]*B[1] + B[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*P[0] + P[1]*A[0]))

    areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

    # Si el area del triangulo es 0, retornar nada para
    # prevenir division por 0.
    if areaABC == 0:
        return None

    # Determinar las coordenadas baricentricas dividiendo el 
    # area de cada subtriangulo por el area del triangulo mayor.
    u = areaPCB / areaABC
    v = areaACP / areaABC
    w = areaABP / areaABC

    # Si cada coordenada esta entre 0 a 1 y la suma de las tres
    # es igual a 1, entonces son validas.
    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and isclose(u+v+w, 1.0):
        return (u, v, w)
    else:
        return None