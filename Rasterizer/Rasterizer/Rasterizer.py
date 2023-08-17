import shaders
from obj import Obj
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 1820    # Ancho en pixeles
height = 920   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.5, 0.5, 0.5)
rend.glClear()


# Se cargan los modelos con sus efectos a renderizar


#A
model1 = Model("trexv2.obj",
              translate = (2,0,-5),                
              rotate = (0,0,0),                    
              scale = (1.5, 1.5, 1.5))
model1.LoadTextures(["trex.bmp", "magma.bmp"])
model1.SetShaders(shaders.vertexShader, shaders.multiTextureShader)
rend.glAddModel(model1)

#B
model2 = Model("trexv2.obj",
               translate = (-2,0,-5),                
               rotate = (0,0,0),                    
               scale = (1.5, 1.5, 1.5))
model2.LoadTextures(["trex.bmp"])
model2.SetShaders(shaders.vertexShader, shaders.StarmanShader)
rend.glAddModel(model2)

#C
model3 = Model("trexv2.obj",
              translate = (0,0,-5),                
              rotate = (0,0,0),                    
              scale = (1.5, 1.5, 1.5))
model3.LoadTextures(["trex.bmp"])
model3.SetShaders(shaders.vertexShader, shaders.trypophobiaShader)
rend.glAddModel(model3)


# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")