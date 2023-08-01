import random
import shaders
from gl import Renderer, V2, V3, color

width = 512
height = 512

rend = Renderer(width,height)

rend.vertexShader= shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

verts = [V3(0,0,0),
         V3(50,0,0),
         V3(25,40,0)]

rend.glAddVertices(verts)

rend.glModelMatrix(translate=(width/2, height/2, 0),
                   rotate=(0,0,0),
                   scale = (5,5,5))

rend.glRender()

rend.glFinish("output.bmp")