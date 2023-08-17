import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.5, 0.5, 0.5)
rend.glClear()


# Se brindan los shaders a utilizar
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.yellowGlowShader


# Cargar el modelo en el renderizador
rend.glLoadModel(filename = "model.obj",              
                 textureName = "model.bmp",           
                 translate = (0,0,-5),                
                 rotate = (0,0,0),                    
                 scale = (2,2,2))


# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")