from myNumpy import matrix_multiplier, matrix_vector_multiplier, dot_product
from math import sin, pi, sqrt
import random

def vertexShader(vertex, **kwargs):

    # El Vertex Shader se lleva a cabo por cada v�rtice
    
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]

    temp1 = matrix_multiplier(vpMatrix, projectionMatrix)
    temp2 = matrix_multiplier(temp1, viewMatrix)
    temp3 = matrix_multiplier(temp2, modelMatrix)

    vt =  matrix_vector_multiplier(temp3, vt)

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt


def fragmentShader(**kwargs):

    # El Fragment Shader se lleva a cabo por cada pixel
    # que se renderizar� en la pantalla.

    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1,1,1)

    return color


def flatShader(**kwargs):
    
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["normals"]

    b = 1.0
    g = 1.0
    r = 1.0
    
    if texture != None:
        textureColor = texture.getColor(texCoords[0], texCoords[1])
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]


    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    b *= intensity
    g *= intensity
    r *= intensity


    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]


def gouradShader(**kwargs):

    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:

        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]
    

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    b *= intensity
    g *= intensity
    r *= intensity


    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]


def toonShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:

        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]
    

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)


    if intensity <= 0.25:
        intensity = 0.2
    elif intensity <= 0.5:
        intensity = 0.45
    elif intensity <= 0.75:
        intensity = 0.7
    elif intensity <= 1.0:
        intensity = 0.95


    b *= intensity
    g *= intensity
    r *= intensity


    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]


def redShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:

        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]
    

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    b *= 0
    g *= 0
    r *= intensity


    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]


def yellowGlowShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    camMatrix = kwargs["camMatrix"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:

        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]
    

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    if intensity <= 0: intensity = 0

    camForward = (camMatrix[0][2],
                  camMatrix[1][2],
                  camMatrix[2][2])

    glowAmount = 1 - dot_product(normal, camForward)

    if glowAmount <=0:
        glowAmount = 0

    yellow = (1,1,0)

    b += glowAmount * yellow[2]
    g += glowAmount * yellow[1]
    r += glowAmount * yellow[0]

    if b >= 1.0: b = 1.0
    if g >= 1.0: g = 1.0
    if r >= 1.0: r = 1.0

    return r, g, b


def StarmanShader(**kwargs):
    # Se extraen los argumentos clave del diccionario kwargs
    textures = kwargs["textures"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    camMatrix = kwargs["camMatrix"]

    # Valores iniciales de color
    b = 1.0
    g = 1.0
    r = 1.0

    # Si hay una textura, se mezcla con el color base
    if textures[0] is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]

        # Se obtiene el color de la textura en las coordenadas tU, tV
        textureColor = textures[0].getColor(tU, tV)

        # Se modifica el color base con los componentes de la textura
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    # Invierte la dirección de la luz para el cálculo de la intensidad
    dLight = list(dLight)
    dLight = [-x for x in dLight]

    # Calcula la intensidad de la luz en función de la normal y la dirección de la luz
    intensity = dot_product(normal, dLight)

    # Si la intensidad es negativa, se establece en cero
    if intensity <= 0:
        intensity = 0

    # Se obtiene la dirección hacia adelante de la cámara desde la matriz de la cámara
    camForward = (camMatrix[0][2],
                  camMatrix[1][2],
                  camMatrix[2][2])

    # Calcula la cantidad de resplandor en función de la normal y la dirección de la cámara
    glowAmount = 1 - dot_product(normal, camForward)

    # Si el resplandor es negativo, se establece en cero
    if glowAmount <= 0:
        glowAmount = 0

    # Efecto de brillo arcoíris basado en las coordenadas de textura
    # Dependiendo de las coordenadas de la diagonal se generan los valores para rojo, verde y azul, que varian a partir de 
    # un valor sinusoidal, esto para generar un cambio sutil en las fases de colores
    diagonalValue = (tU + tV) * 0.5                     # Calcula el valor diagonal promedio en coordenadas de textura
    rGlow = abs(sin(diagonalValue * 2 * pi))            # Calcula el componente rojo del brillo arcoíris
    gGlow = abs(sin((diagonalValue + 1/3.0) * 2 * pi))  # Calcula el componente verde del brillo arcoíris
    bGlow = abs(sin((diagonalValue + 2/3.0) * 2 * pi))  # Calcula el componente azul del brillo arcoíris

    # Se agrega el brillo arcoíris al color base, ponderado por el resplandor
    b += glowAmount * bGlow  # Agrega brillo azul arcoíris con resplandor ponderado
    g += glowAmount * gGlow  # Agrega brillo verde arcoíris con resplandor ponderado
    r += glowAmount * rGlow  # Agrega brillo rojo arcoíris con resplandor ponderado


    # Asegura que los componentes de color no excedan 1.0
    if b >= 1.0:
        b = 1.0
    if g >= 1.0:
        g = 1.0
    if r >= 1.0:
        r = 1.0

    # Retorna los componentes de color modificados
    return r, g, b



def multiTextureShader(**kwargs):
    tA, tB, tC = kwargs["texCoords"]
    textures = kwargs["textures"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]
    
    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    color_final = [0, 0, 0]
    
    for texture in textures:
        if texture != None:
            textureColor = texture.getColor(tU, tV)
            
            color_final[0] = max(color_final[0], textureColor[0] * intensity)
            color_final[1] = max(color_final[1], textureColor[1] * intensity)
            color_final[2] = max(color_final[2], textureColor[2] * intensity)


    # Verificar que la intensidad sea mayor que 0 para devolver los valores, si no, devolver [0,0,0]
    if intensity > 0:
        return color_final
    else:
        return [0,0,0]



def trypophobiaShader(**kwargs):

    textures = kwargs["textures"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    verts = kwargs["verts"] # se asume que tienes los vértices

    # Calcular el centroide del triángulo
    centroid = [(v[0] + v[1] + v[2]) / 3 for v in zip(*verts)]
    
    # Utilizar el centroide para determinar si renderizar o no
    random.seed(str(centroid))  # usa el centroide como semilla
    if random.random() < 0.20:  # 10% de probabilidad de ser transparente
        return 0.5, 0.5, 0.5

    # Tomamos la normal promedio de la cara, no interpolada
    normal = [sum(x) for x in zip(nA, nB, nC)]
    magnitude = sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
    normal = [n/magnitude for n in normal]  # normalizamos

    # Color base como en Minecraft
    b = 1.0
    g = 1.0
    r = 1.0

    # Si hay una textura, se mezcla con el color base
    if textures[0] is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = textures[0].getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    dLight = [-x for x in dLight]  # invierte la dirección de la luz
    intensity = dot_product(normal, dLight)
    
    if intensity <= 0:
        intensity = 0

    # Asegura que los componentes de color no excedan 1.0
    b = min(b * intensity, 1.0)
    g = min(g * intensity, 1.0)
    r = min(r * intensity, 1.0)

    return r, g, b


