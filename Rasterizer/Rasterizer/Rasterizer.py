import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 1024    # Ancho en pixeles
height = 1024   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida
rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader


# Cargar el modelo en el renderizador
rend.glLoadModel("model.obj",                       # Archivo a cargar
                 translate=(width/2,height/2,0),    # Cambiar los valores de posicion x,y dependiendo de donde se quiera colocar el modelo (z se deja en 0)
                 rotate=(0,180,0),                    # Cambiar los valores de los �ngulos EN GRADOS para rotar el modelo en los ejes x,y,z respectivamente
                 scale = (400,400,400))             # Cambiar los valores para agrandar el modelo en los ejes x,y,z, siendo 1,1,1 su tama�o original

# Renderizar el modelo en la imagen
rend.glRender()

rend.glFinish("output.bmp")