import shaders
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)

rend.glBackgroundTexture("backgrounds/space.bmp")
rend.glClearBackground()

# Se mueve la posicion de la luz
rend.directionalLight = (0,0,-1)


# Se cargan los modelos con sus efectos a renderizar
model1 = Model("models/model.obj",
              translate = (0,0,-5),                
              rotate = (0,50,0),                    
              scale = (1.5, 1.5, 1.5))
model1.LoadTexture("textures/model.bmp")
model1.SetShaders(shaders.vertexShader, shaders.StarmanShader)
rend.glAddModel(model1)

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")