from myNumpy import cross_product, matrix_multiplier, matrix_vector_multiplier, dot_product, vector_normalize
from math import sqrt

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

    # Calculate the texture coordinates
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

    # Check if the intensity is greater than 0 to return the values, otherwise return [0,0,0]
    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]