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