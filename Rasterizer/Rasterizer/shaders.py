from myNumpy import cross_product, matrix_multiplier, matrix_vector_multiplier, dot_product, vector_normalize
from math import sin, sqrt, pi, atan2, floor

# Funcion que evita que los colores se pasen de los limites establecidos
def clamp(value, min_val=0.0, max_val=1.0):
    return max(min_val, min(value, max_val))

#---------------------------------------Vertex Shaders---------------------------------------

def vertexShader(vertex, **kwargs):

    # El Vertex Shader se lleva a cabo por cada vertice
    
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


def fatShader(vertex, **kwargs):

    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]
    normal = kwargs["normal"]

    blowAmount = 0.2

    vt = [vertex[0] + (normal[0] * blowAmount),
          vertex[1] + (normal[1] * blowAmount),
          vertex[2] + (normal[2] * blowAmount),
          1]

    temp1 = matrix_multiplier(vpMatrix, projectionMatrix)
    temp2 = matrix_multiplier(temp1, viewMatrix)
    temp3 = matrix_multiplier(temp2, modelMatrix)

    vt =  matrix_vector_multiplier(temp3, vt)

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

#--------------------------------------Fragment Shaders--------------------------------------

def fragmentShader(**kwargs):

    # El Fragment Shader se lleva a cabo por cada pixel
    # que se renderizara en la pantalla.

    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
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


    return r, g, b


def flatShader(**kwargs):
    
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    nA, nB, nC = kwargs["normals"]
    tA, tB, tC = kwargs["texCoords"]
    u, v, w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]

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

    normal = [sum(x) for x in zip(nA, nB, nC)]
    normal = vector_normalize(normal)

    normal.append(0.0)

    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    if intensity <= 0:
        intensity = 0

    # Asegura que los componentes de color no excedan 1.0
    b = min(b * intensity, 1.0)
    g = min(g * intensity, 1.0)
    r = min(r * intensity, 1.0)

    return r, g, b


def gouradShader(**kwargs):

    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]

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
              u * nA[2] + v * nB[2] + w * nC[2],
              0]
    
    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]


    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    b *= intensity
    g *= intensity
    r *= intensity

    b = clamp(b)
    g = clamp(g)
    r = clamp(r)

    if intensity > 0:
        return r, g, b
    else:
        return [0,0,0]


def normalMapShader(**kwargs):
    texture = kwargs["texture"]
    normalMap = kwargs["normalMap"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]
    tangent = kwargs["tangent"]

    b = 1.0
    g = 1.0
    r = 1.0

    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]


    if texture != None:
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2],
                0]
    
    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]

    dLight = list(dLight)
    dLight = [-x for x in dLight]

    if normalMap:
        texNormal = normalMap.getColor(tU, tV)
        texNormal = [texNormal[0] * 2 - 1,
                     texNormal[1] * 2 - 1,
                     texNormal[2] * 2 - 1]

        texNormal = vector_normalize(texNormal)

        tangent = [tangent[0], tangent[1], tangent[2], 0]
        tangent = matrix_vector_multiplier(modelMatrix, tangent)
        tangent = [tangent[0], tangent[1], tangent[2]]

        bitangent = cross_product(normal, tangent)
        bitangent = vector_normalize(bitangent)

        tangent = cross_product(normal, bitangent)
        tangent = vector_normalize(tangent)

        tangentMatirx = [[tangent[0], bitangent[0], normal[0]],
                         [tangent[1], bitangent[1], normal[1]],
                         [tangent[2], bitangent[2], normal[2]]]

        texNormal = matrix_vector_multiplier(tangentMatirx, texNormal)
        texNormal = vector_normalize(texNormal)

        normal = texNormal

    
    intensity = dot_product(normal,dLight)
    
    intensity = clamp(intensity)

    b *= intensity
    g *= intensity
    r *= intensity

    b = clamp(b)
    g = clamp(g)
    r = clamp(r)

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
    modelMatrix = kwargs["modelMatrix"]


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
              u * nA[2] + v * nB[2] + w * nC[2],
              0]
    
    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]

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

    b = clamp(b)
    g = clamp(g)
    r = clamp(r)

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
    modelMatrix = kwargs["modelMatrix"]

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
              u * nA[2] + v * nB[2] + w * nC[2],
              0]
    
    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    
    b *= 0
    g *= 0
    r *= intensity

    b = clamp(b)
    g = clamp(g)
    r = clamp(r)

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
    modelMatrix = kwargs["modelMatrix"]

    b = 1.0
    g = 1.0
    r = 1.0

    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]

    if texture != None:
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2],
              0]
    
    normal =  matrix_vector_multiplier(modelMatrix,normal) 
    normal = [normal[0], normal[1], normal[2]]

    camForward = (camMatrix[0][2],
                  camMatrix[1][2],
                  camMatrix[2][2])

    # El primer valor se puede variar para que el brillo ocupe mas o menos del model
    glowAmount = 1 - dot_product(normal, camForward)

    if glowAmount <=0:
        glowAmount = 0

    yellow = (1,1,0)

    b += glowAmount * yellow[2]
    g += glowAmount * yellow[1]
    r += glowAmount * yellow[0]

    b = min(b, 1.0)
    g = min(g, 1.0)
    r = min(r, 1.0)

    return r, g, b


def multiTextureShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]
    extraTex = kwargs["extraTexture"]

    b = 1.0
    g = 1.0
    r = 1.0

    # Calcula las coordenadas de textura
    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]

    if texture != None:
        textureColor = texture.getColor(tU, tV)
        r *= textureColor[0]
        g *= textureColor[1]
        b *= textureColor[2]

    # Obtener el color de la textura extra
    if extraTex != None:
        extraColor = extraTex.getColor(tU, tV)
        extraR = extraColor[0]
        extraG = extraColor[1]
        extraB = extraColor[2]
    else:
        extraR = 1.0
        extraG = 1.0
        extraB = 1.0
    
    # Mezcla de colores
    blendFactor = 0.5
    r = (r * blendFactor) + (extraR * (1 - blendFactor))
    g = (g * blendFactor) + (extraG * (1 - blendFactor))
    b = (b * blendFactor) + (extraB * (1 - blendFactor))

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2],
              0]
    
    normal = matrix_vector_multiplier(modelMatrix, normal)
    normal = [normal[0], normal[1], normal[2]]

    # Se transforma la direccion de luz
    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)
    
    r *= intensity
    g *= intensity
    b *= intensity

    # Limitando a valores permitidos los valores r,g,b
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    # Revisa si la intensidad es mayor a 0 de lo contrario retorna negro
    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def GlowPatternsShader(glowType, **kwargs):
    # Se extraen los argumentos clave del diccionario kwargs
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    camMatrix = kwargs["camMatrix"]
    modelMatrix = kwargs["modelMatrix"]

    # Valores iniciales de color
    b = 1.0
    g = 1.0
    r = 1.0

    tU = u * tA[0] + v * tB[0] + w * tC[0]
    tV = u * tA[1] + v * tB[1] + w * tC[1]

    # Si hay una textura, se mezcla con el color base
    if texture != None:
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2],
              0]

    normal = matrix_vector_multiplier(modelMatrix, normal)
    normal = [normal[0], normal[1], normal[2]]

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    # Si la intensidad es negativa, se establece en cero
    if intensity <= 0:
        intensity = 0

    # Se obtiene la direccion hacia adelante de la camara desde la matriz de la camara
    camForward = (camMatrix[0][2],
                  camMatrix[1][2],
                  camMatrix[2][2])

    # Calcula la cantidad de resplandor en funcion de la normal y la direccion de la camara
    glowAmount = 1.4 - dot_product(normal, camForward)
    
    # Si el brillo es negativo, se establece en cero
    if glowAmount <= 0:
        glowAmount = 0

    # Efecto de brillo basado en las coordenadas de textura
    # Dependiendo de las coordenadas se generan los valores para rojo, verde y azul, que varian a partir de 
    # un valor sinusoidal, esto para generar un cambio sutil en las fases de colores

    # Calcula el valor diagonal promedio en coordenadas de textura                   
    diagonalValue = (tU + tV) * 0.5 

    if glowType == "starman":# Efecto arcoiris
        rGlow = abs(sin(diagonalValue * 2 * pi))            
        gGlow = abs(sin((diagonalValue + 1/3.0) * 2 * pi))  
        bGlow = abs(sin((diagonalValue + 2/3.0) * 2 * pi))

    elif glowType == "infernix":# Efecto escudo para "los malos"
        rGlow = abs(sin(intensity * 2 * pi))
        gGlow = 0
        bGlow = 0 
        maxGreen = 0.5  
        gGlow = min(gGlow, maxGreen)

    elif glowType == "celestia":# Efecto escudo para "los buenos"
        rGlow = 0  
        gGlow = abs(sin((diagonalValue + 1/3.0) * 2 * pi)) * 0.5  
        bGlow = abs(sin((diagonalValue + 2/3.0) * 2 * pi))


    # Interpolacion de colores para difuminar el brillo
    b += glowAmount * bGlow 
    g += glowAmount * gGlow  
    r += glowAmount * rGlow  

    # Limitando a valores permitidos los valores r,g,b
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    # Retorna los componentes de color modificados
    return r, g, b

def ThermalCamShader(thermal, **kwargs):
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]
    camMatrix = kwargs["camMatrix"]
    modelMatrix = kwargs["modelMatrix"]

    # Referencia de la paleta iron. https://jsfiddle.net/ozkh6bp1
    iron_palette = [
        (0, 0, 0),(0, 0, 36),(0, 0, 51),(0, 0, 66),(0, 0, 81),(2, 0, 90),(4, 0, 99),(7, 0, 106),(11, 0, 115),(14, 0, 119),(20, 0, 123),
        (27, 0, 128),(33, 0, 133),(41, 0, 137),(48, 0, 140),(55, 0, 143),(61, 0, 146),(66, 0, 149),(72, 0, 150),(78, 0, 151),(84, 0, 152),
        (91, 0, 153),(97, 0, 155),(104, 0, 155),(110, 0, 156),(115, 0, 157),(122, 0, 157),(128, 0, 157),(134, 0, 157),(139, 0, 157),
        (146, 0, 156),(152, 0, 155),(157, 0, 155),(162, 0, 155),(167, 0, 154),(171, 0, 153),(175, 1, 152),(178, 1, 151),(182, 2, 149),
        (185, 4, 149),(188, 5, 147),(191, 6, 146),(193, 8, 144),(195, 11, 142),(198, 13, 139),(201, 17, 135),(203, 20, 132),(206, 23, 127),
        (208, 26, 121),(210, 29, 116),(212, 33, 111),(214, 37, 103),(217, 41, 97),(219, 46, 89),(221, 49, 78),(223, 53, 66),(224, 56, 54),
        (226, 60, 42),(228, 64, 30),(229, 68, 25),(231, 72, 20),(232, 76, 16),(234, 78, 12),(235, 82, 10),(236, 86, 8),(237, 90, 7),
        (238, 93, 5),(239, 96, 4),(240, 100, 3),(241, 103, 3),(241, 106, 2),(242, 109, 1),(243, 113, 1),(244, 116, 0),(244, 120, 0),
        (245, 125, 0),(246, 129, 0),(247, 133, 0),(248, 136, 0),(248, 139, 0),(249, 142, 0),(249, 145, 0),(250, 149, 0),(251, 154, 0),
        (252, 159, 0),(253, 163, 0),(253, 168, 0),(253, 172, 0),(254, 176, 0),(254, 179, 0),(254, 184, 0),(254, 187, 0),(254, 191, 0),
        (254, 195, 0),(254, 199, 0),(254, 202, 1),(254, 205, 2),(254, 208, 5),(254, 212, 9),(254, 216, 12),(255, 219, 15),(255, 221, 23),
        (255, 224, 32),(255, 227, 39),(255, 229, 50),(255, 232, 63),(255, 235, 75),(255, 238, 88),(255, 239, 102),(255, 241, 116),
        (255, 242, 134),(255, 244, 149),(255, 245, 164),(255, 247, 179),(255, 248, 192),(255, 249, 203),(255, 251, 216),(255, 253, 228),
        (255, 254, 239)]

    # Interpolacion de valores
    def lerp(a, b, t):
        return a + (b - a) * t
    
    # Valores iniciales de color
    b = 1.0
    g = 1.0
    r = 1.0

    # Se calcula la normal para el punto
    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2],
              0]

    normal = matrix_vector_multiplier(modelMatrix, normal)
    normal = [normal[0], normal[1], normal[2]]

    dLight = list(dLight)
    dLight = [-x for x in dLight]
    intensity = dot_product(normal, dLight)

    # Si la intensidad es negativa, se establece en cero
    if intensity <= 0:
        intensity = 0

    # Se obtiene la direccion hacia adelante de la camara desde la matriz de la camara
    camForward = (camMatrix[0][2],
                  camMatrix[1][2],
                  camMatrix[2][2])

    # Modificacion de paleta segun opcion
    if thermal == 'a':
        glowAmount = 1.2 - dot_product(normal, camForward)
    elif thermal == 'b':
        glowAmount = 1.6 - dot_product(normal, camForward)
        iron_palette = iron_palette[::-1]


    if glowAmount <= 0:
        glowAmount = 0

    # Normaliza glowAmount al rango [0, 1]
    glowAmount = clamp(glowAmount)

    # Mapeo de colores basados en la paleta
    index1 = int(glowAmount * (len(iron_palette) - 1))
    index2 = min(index1 + 1, len(iron_palette) - 1)

    color1 = iron_palette[index1]
    color2 = iron_palette[index2]

    # Calcula el factor de interpolacion
    t = glowAmount * (len(iron_palette) - 1) - index1

    # Interpola entre los dos colores
    color = (
        int(lerp(color1[0], color2[0], t)),
        int(lerp(color1[1], color2[1], t)),
        int(lerp(color1[2], color2[2], t))
    )

    r *= color[0]
    g *= color[1]
    b *= color[2]

    # Limitando a valores permitidos los valores r,g,b
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    # Retorna los componentes de color modificados
    return r, g, b