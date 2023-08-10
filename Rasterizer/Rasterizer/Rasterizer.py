import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 1920    # Ancho en pixeles
height = 1080   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida
rend = Renderer(width, height)

# Se brindan los shaders a utilizar
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader



## Medium Shot
#rend.glLookAt(camPos=(0, 3, 0),
#              eyePos=(0, 0, -5))


#rend.glLoadModel(filename = "pot.obj",              
#                 textureName = "pot.bmp",           
#                 translate = (0,-2,-5),                
#                 rotate = (0,0,0),                    
#                 scale = (8,8,8))



# Low Angle
rend.glLookAt(camPos=(1, -5, 0),
              eyePos=(0, 0, -5))


rend.glLoadModel(filename = "pot.obj",              
                 textureName = "pot.bmp",           
                 translate = (0,-1,-5),                
                 rotate = (0,0,0),                    
                 scale = (10,10,10))


## High Angle
#rend.glLookAt(camPos=(-2, 3, 0),
#              eyePos=(0, 0, -5))


#rend.glLoadModel(filename = "model.obj",              
#                 textureName = "model.bmp",           
#                 translate = (0,0,-5),                
#                 rotate = (0,0,0),                    
#                 scale = (2,2,2))




## Dutch Angle
#rend.glLookAt(camPos=(-2, -1, 0),
#              eyePos=(0, 0, -5))


#rend.glLoadModel(filename = "model.obj",              
#                 textureName = "model.bmp",           
#                 translate = (0,0,-5),                
#                 rotate = (0,0,25),                    
#                 scale = (2,2,2))

rend.glRender()

rend.glFinish("output2.bmp")

