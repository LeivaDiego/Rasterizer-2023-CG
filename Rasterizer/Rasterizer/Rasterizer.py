import shaders
from obj import Obj
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 1000    # Ancho en pixeles
height = 540   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)
rend.glClear()


# Se cargan los modelos con sus efectos a renderizar

model1 = Model("model.obj",
              translate = (0,0,-5),                
              rotate = (0,0,0),                    
              scale = (1.5, 1.5, 1.5))
model1.LoadTexture("model.bmp")
model1.SetShaders(shaders.vertexShader, shaders.yellowGlowShader)
rend.glAddModel(model1)

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")