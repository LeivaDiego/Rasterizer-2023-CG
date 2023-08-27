import shaders
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)

# Seleccionar el fondo de la imagen
rend.glBackgroundTexture("backgrounds/orbit.bmp")
rend.glClearBackground()


# Se mueve la posicion de la luz
rend.directionalLight = (0,0,-1)



# Carga de modelos con sus respectivos shaders a renderizar

#-----------------------------Modelos Principales------------------------------

# Las naves buenas------------------------------------------------------------- 

ak5 = Model("models/ak5.obj",
            translate = (-2.3, -1.6, -6),
            rotate = (10, -15, -35),
            scale = (1, 1, 1))
ak5.LoadTexture("textures/ak5.bmp")
ak5.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(ak5)


mk6 = Model("models/mk6.obj",
            translate = (-3.5, 0, -5),
            rotate = (15, 0, -50),
            scale = (1, 1, 1))
mk6.LoadTexture("textures/mk6.bmp")
mk6.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(mk6)
#------------------------------------------------------------------------------


# Las naves malas--------------------------------------------------------------

# la nave nodriza
luminaris = Model("models/luminaris.obj",
            translate = (4, 2, -7),
            rotate = (30, -45, -30),
            scale = (2, 2, 2))
luminaris.LoadTexture("textures/luminaris.bmp")
luminaris.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(luminaris)


# Los trident se repiten con diferente textura (son escoltas)
trident1 = Model("models/trident.obj",
            translate = (5, -1.5, -7),
            rotate = (35, -45, -25),
            scale = (1.3, 1.3, 1.3))
trident1.LoadTexture("textures/trident_toy.bmp")
trident1.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(trident1)

trident2 = Model("models/trident.obj",
            translate = (-1, 2.8, -7),
            rotate = (30, -10, -40),
            scale = (1.5, 1.5, 1.5))
trident2.LoadTexture("textures/trident_cam.bmp")
trident2.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(trident2)

#------------------------------------------------------------------------------



#------------------------------Modelos Secundarios-----------------------------

# SFX--------------------------------------------------------------------------

laser_mk6a = Model("models/laser.obj",
            translate = (-2.3,0.1, -6),
            rotate = (12, -8, -35),
            scale = (0.6, 0.6, 0.6))
laser_mk6a.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_mk6a)

laser_mk6b = Model("models/laser.obj",
            translate = (-2.5,1.5, -6),
            rotate = (24, -8, -35),
            scale = (0.6, 0.6, 0.6))
laser_mk6b.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_mk6b)


laser_ak5 = Model("models/laser.obj",
            translate = (0, 0, -6),
            rotate = (10, -15, -35),
            scale = (1, 1, 1))
laser_ak5.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_ak5)



laser_trident = Model("models/laser.obj",
                translate = (-3.6, 1, -7),
                rotate = (30, -10, -40),
                scale = (1, 1, 1))
laser_trident.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_trident)



laser_luminaris1 = Model("models/laser.obj",
                  translate = (3.5, 0, -7),
                  rotate = (30, -50, -30),
                  scale = (2, 2, 2))
laser_luminaris1.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_luminaris1)

laser_luminaris2 = Model("models/laser.obj",
                  translate = (0.5, 1.5, -7),
                  rotate = (30, -40, -30),
                  scale = (2, 2, 2))
laser_luminaris2.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(laser_luminaris2)


explode = Model("models/fire.obj",
            translate = (5, -1.5, -7),
            rotate = (35, -45, -25),
            scale = (1.3, 1.3, 1.3))
explode.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(explode)
#------------------------------------------------------------------------------

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")