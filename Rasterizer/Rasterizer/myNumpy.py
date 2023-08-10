from math import isclose, sqrt

def barycentricCoords(A, B, C, P):
    
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
        return (-1,-1,-1)


def matrix_multiplier(matrixA, matrixB):
    # Filas y columnas de cada matriz
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])

    # Verificar si las matrices son multiplicables
    if colsA != rowsB:
        raise ValueError("Las dimensiones de las matrices no permiten su multiplicación.")

    # Crear una matriz vacía para almacenar el resultado
    matrixC = [[0 for _ in range(colsB)] for _ in range(rowsA)]
    # Realizar la multiplicación de matrices
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
    return matrixC


def matrix_vector_multiplier(matrix, vector):
    # Tamaños de la matriz y el vector
    rows = len(matrix)
    cols = len(matrix[0])
    size = len(vector)

    # Verificar si la matriz y el vector son multiplicables
    if cols != size:
        raise ValueError("Las dimensiones de la matriz y el vector no permiten su multiplicación.")

    # Se crea el vector vacío para almacenar resultados
    newVector = [0 for _ in range(rows)]

    # Realizar la multiplicación
    for i in range(rows):
        for j in range(cols):
            newVector[i] += matrix[i][j] * vector[j]
    return newVector


def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def inverse_matrix(matrix):
    n = len(matrix)
    augmented_matrix = [row + identity_matrix(n)[i] for i, row in enumerate(matrix)]

    for i in range(n):
        pivot = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    inverse = [row[n:] for row in augmented_matrix]
    return inverse


def cross_product(vecA, vecB):
    if len(vecA) != 3 or len(vecB) != 3:
        raise ValueError("Los vectores deben ser de 3 componentes.")
    
    result = [
        vecA[1] * vecB[2] - vecA[2] * vecB[1],
        vecA[2] * vecB[0] - vecA[0] * vecB[2],
        vecA[0] * vecB[1] - vecA[1] * vecB[0]
    ]
    return result


def vector_normalize(vector):
    magnitude = sqrt(sum(component ** 2 for component in vector))
    normalized_vector = [component / magnitude for component in vector]
    return normalized_vector


def subtract_vector(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise ValueError("Los vectores deben tener la misma longitud.")
    return [a - b for a, b in zip(vectorA, vectorB)]