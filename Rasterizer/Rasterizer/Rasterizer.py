import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 3000    # Ancho en pixeles
height = 1200   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida
rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader


# Cargar el modelo en el renderizador
#rend.glLoadModel(filename = "model.obj",              Archivo del modelo a cargar
#                 textureName = "texture.bmp",         Archivo de la textura del modelo
#                 translate = (width/2, height/2, 0),  Cambiar los valores de posicion x,y dependiendo de donde se quiera colocar el modelo (z se deja en 0)
#                 rotate = (0, 0, 0),                  Cambiar los valores de los angulos EN GRADOS para rotar el modelo en los ejes x,y,z respectivamente
#                 scale = (1, 1, 1))                   Cambiar los valores para agrandar el modelo en los ejes x,y,z, siendo 1,1,1 su tamano original


# Esquina superior izquierda
# De perfil
rend.glLoadModel(filename = "Irex.obj",                                     
                 textureName = "Body_albino.bmp",                          
                 translate = (2 * width/6, height/2 + 50, 0),              
                 rotate = (0, 90, 0),                                    
                 scale = (1, 1, 1))                                        
                          
# Esquina inferior izquierda
# De abajo
rend.glLoadModel(filename = "Irex.obj",               
                 textureName = "Body_albino.bmp",     
                 translate = (2 * width/6, 2 * height/10, 0),              
                 rotate = (0, 90, 90),                             
                 scale = (1, 1, 1))                              

# Esquina inferior derecha
# De frente
rend.glLoadModel(filename = "Irex.obj",                
                 textureName = "Body_albino.bmp",     
                 translate = (5 * width/6, height/10 - 50, 0),             
                 rotate = (0, 180, 0),                            
                 scale = (1, 1, 1))                               

# Esquina superior derecha
# De frente
rend.glLoadModel(filename = "Irex.obj",               
                 textureName = "Body_albino.bmp",    
                 translate = (5 * width/6, height/2 + 50, 0),             
                 rotate = (0, 0, 0),                             
                 scale = (1, 1, 1))   

# Renderizar el modelo en la imagen
rend.glRender()

# Generar la imagen
rend.glFinish("output.bmp")