import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 4000    # Ancho en pixeles
height = 2160   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida
rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader


# Cargar el modelo en el renderizador
rend.glLoadModel(filename = "Irex.obj",              # Archivo del modelo a cargar
                 textureName = "Body-TM_albino.bmp",           # Archivo de la textura del modelo
                 translate = (width/2,height/6,0),    # Cambiar los valores de posicion x,y dependiendo de donde se quiera colocar el modelo (z se deja en 0)
                 rotate = (0,90,0),                   # Cambiar los valores de los �ngulos EN GRADOS para rotar el modelo en los ejes x,y,z respectivamente
                 scale = (3,3,3))               # Cambiar los valores para agrandar el modelo en los ejes x,y,z, siendo 1,1,1 su tama�o original


# Renderizar el modelo en la imagen
rend.glRender()

rend.glFinish("output.bmp")