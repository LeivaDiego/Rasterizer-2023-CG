
from myNumpy import matrix_multiplier, matrix_vector_multiplier


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

#def fragmentShader(**kwargs):

#    # El Fragment Shader se lleva a cabo por cada pixel
#    # que se renderizar� en la pantalla.

#    texCoords = kwargs["texCoords"]
#    texture = kwargs["texture"]

#    if texture != None:
#        color = texture.getColor(texCoords[0], texCoords[1])
#    else:
#        color = (1,1,1)

#    return color


def multiTextureShader(**kwargs):
    texCoords = kwargs["texCoords"]
    textures = kwargs["textures"] # Lista de texturas

    color_final = [0, 0, 0]

    # Iterar sobre cada textura y combinar su color (por ejemplo, promedio)
    for texture in textures:
        if texture != None:
            color = texture.getColor(texCoords[0], texCoords[1])
            color_final[0] += color[0]
            color_final[1] += color[1]
            color_final[2] += color[2]

    color_final[0] /= len(textures)
    color_final[1] /= len(textures)
    color_final[2] /= len(textures)

    return color_final