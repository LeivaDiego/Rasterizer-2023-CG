import shaders
from obj import Obj
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)
rend.glClear()

#rend.glBackgroundTexture("backgrounds/space.bmp")
#rend.glClearBackground()

# Se mueve la posicion de la luz
rend.directionalLight = (0,0,-1)


# Se cargan los modelos con sus efectos a renderizar
model1 = Model("models/model.obj",
              translate = (-1,0,-5),                
              rotate = (0,0,0),                    
              scale = (1.5, 1.5, 1.5))
model1.LoadTexture("textures/model.bmp")
model1.LoadNormalMap("normals/model_normal.bmp")
model1.SetShaders(shaders.vertexShader, shaders.normalMapShader)
rend.glAddModel(model1)


model2 = Model("models/model.obj",
              translate = (1,0,-5),                
              rotate = (0,0,0),                    
              scale = (1.5, 1.5, 1.5))
model2.LoadTexture("textures/model.bmp")
model2.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(model2)

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")