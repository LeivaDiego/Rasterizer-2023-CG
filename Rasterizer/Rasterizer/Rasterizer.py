import shaders
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 2560    # Ancho en pixeles
height = 1440   # Alto en pixeles


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)

# Seleccionar el fondo de la imagen
rend.glBackgroundTexture("backgrounds/orbit.bmp")
rend.glClearBackground()


# Se mueve la posicion de la luz
rend.directionalLight = (-1,0,-1)



# Carga de modelos con sus respectivos shaders a renderizar

#-----------------------------Modelos Principales------------------------------
# El shader Ultra shader es la combinacion de 2 shaders en 1
# (textura multiple, efectos de escudos)
# Las naves buenas------------------------------------------------------------- 

ak5 = Model("models/ak5.obj",
            translate = (-2.3, -1.6, -6),
            rotate = (10, -18, -35),
            scale = (1, 1, 1))
ak5.LoadTexture("textures/ak5.bmp")
ak5.SetShaders(shaders.vertexShader, lambda **kwargs: shaders.ShieldShader(glowType="celestia", **kwargs))
rend.glAddModel(ak5)


mk6 = Model("models/mk6.obj",
            translate = (-3.5, 0, -5),
            rotate = (15, 0, -50),
            scale = (1, 1, 1))
mk6.LoadTexture("textures/mk6.bmp")
mk6.LoadExtraTexture("textures/rayo.bmp")
mk6.SetShaders(shaders.vertexShader, shaders.multiTextureShader)
rend.glAddModel(mk6)
#------------------------------------------------------------------------------


# Las naves malas--------------------------------------------------------------

# la nave nodriza
luminaris = Model("models/luminaris.obj",
            translate = (4, 2, -7),
            rotate = (30, -45, -30),
            scale = (2, 2, 2))
luminaris.LoadTexture("textures/luminaris.bmp")
luminaris.LoadExtraTexture("textures/infernix.bmp")
luminaris.SetShaders(shaders.vertexShader, lambda **kwargs: shaders.UltraShader(glowType="infernix", **kwargs))
rend.glAddModel(luminaris)


# Los trident se repiten con diferente textura (son escoltas)

# Nave con normal mapping
trident1 = Model("models/trident.obj",
            translate = (5, -1.5, -7),
            rotate = (35, -45, -25),
            scale = (1.3, 1.3, 1.3))
trident1.LoadTexture("textures/trident_cam.bmp")
trident1.SetShaders(shaders.waveShader, shaders.TrypophobiaShader)
rend.glAddModel(trident1)

trident2 = Model("models/trident.obj",
            translate = (-1, 2.8, -7),
            rotate = (30, -10, -40),
            scale = (1.5, 1.5, 1.5))
trident2.LoadTexture("textures/trident_toy.bmp")
trident2.LoadExtraTexture("normals/trident_normal.bmp")
trident2.SetShaders(shaders.twistShader, shaders.normalMapShader)
rend.glAddModel(trident2)

#------------------------------------------------------------------------------



#------------------------------Modelos Secundarios-----------------------------

# SFX--------------------------------------------------------------------------

laser_mk6a = Model("models/laser.obj",
            translate = (-2.3,0.1, -6),
            rotate = (12, -8, -35),
            scale = (0.6, 0.6, 0.6))
laser_mk6a.SetShaders(shaders.twistShader, lambda **kwargs: shaders.BlastShader(glowColor=[0, 255, 0], **kwargs))
rend.glAddModel(laser_mk6a)

laser_mk6b = Model("models/laser.obj",
            translate = (-2.5,1.5, -6),
            rotate = (24, -8, -35),
            scale = (0.6, 0.6, 0.6))
laser_mk6b.SetShaders(shaders.twistShader, lambda **kwargs: shaders.BlastShader(glowColor=[0, 255, 0], **kwargs))
rend.glAddModel(laser_mk6b)


laser_ak5 = Model("models/laser.obj",
            translate = (-1, -1, -6),
            rotate = (8, -18, 0),
            scale = (1, 1, 1))
laser_ak5.SetShaders(shaders.twistShader,  lambda **kwargs: shaders.BlastShader(glowColor=[0, 255, 0], **kwargs))
rend.glAddModel(laser_ak5)



laser_trident = Model("models/laser.obj",
                translate = (-3.6, 1, -7),
                rotate = (30, -10, -40),
                scale = (1, 1, 1))
laser_trident.SetShaders(shaders.waveShader,  lambda **kwargs: shaders.BlastShader(glowColor=[255, 0, 10], **kwargs))
rend.glAddModel(laser_trident)



laser_luminaris1 = Model("models/laser.obj",
                  translate = (3.5, 0, -7),
                  rotate = (30, -50, -30),
                  scale = (2, 2, 2))
laser_luminaris1.SetShaders(shaders.waveShader,  lambda **kwargs: shaders.BlastShader(glowColor=[255, 0, 0], **kwargs))
rend.glAddModel(laser_luminaris1)

laser_luminaris2 = Model("models/laser.obj",
                  translate = (0.5, 1.5, -7),
                  rotate = (30, -40, -30),
                  scale = (2, 2, 2))
laser_luminaris2.SetShaders(shaders.waveShader,  lambda **kwargs: shaders.BlastShader(glowColor=[255, 0, 0], **kwargs))
rend.glAddModel(laser_luminaris2)


explode = Model("models/fire.obj",
            translate = (5, -1.5, -7),
            rotate = (35, -45, -25),
            scale = (1.3, 1.3, 1.3))
explode.LoadExtraTexture("textures/sun.bmp")
explode.SetShaders(shaders.waveShader,  shaders.multiTextureShader)
rend.glAddModel(explode)
#------------------------------------------------------------------------------

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")