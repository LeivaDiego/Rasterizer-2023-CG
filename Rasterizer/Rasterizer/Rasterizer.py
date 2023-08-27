import shaders
from gl import Renderer, Model

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles


# Inicializar el Renderer con la resolucion definida y color de fondo
rend = Renderer(width, height)
rend.glClearColor(0.2, 0.2, 0.2)

rend.glBackgroundTexture("backgrounds/orbit.bmp")
rend.glClearBackground()

# Se mueve la posicion de la luz
rend.directionalLight = (0,0,-1)

#-----------------------------Modelos Principales-----------------------------

# Las naves buenas------------------------------------------------------------ 

ak5 = Model("models/ak5.obj",
            translate = (-2.3, -1.6, -6),
            rotate = (10, -10, -35),
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
            translate = (0, 2.8, -7),
            rotate = (30, -10, -40),
            scale = (1.5, 1.5, 1.5))
trident2.LoadTexture("textures/trident_cam.bmp")
trident2.SetShaders(shaders.vertexShader, shaders.gouradShader)
rend.glAddModel(trident2)

#------------------------------------------------------------------------------

# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output.bmp")