import random
from gl import Renderer, V2, color

width = 1920
height = 1080

rend = Renderer(width,height)

# Line Pattern
#for x in range(0, width, 25):
#    rend.glLine(V2(0,0), V2(x,height - 1))
#for x in range(0, width, 25):
#    rend.glLine(V2(0, height - 1), V2(x,0))

# Static
#for x in range(width):
#    for y in range(height):
#        if random.random() > 0.5:
#            rend.glPoint(x,y)

# Color Static
#for x in range(width):
#    for y in range(height): 
#        rend.glPoint(x,y,color(random.random(),
#                               random.random(),
#                               random.random()))

# Star
for x in range(width):
    for y in range(height):
        if random.random() > 0.995:
            size = random.randrange(0,3)
            brigthness = random.random() / 2 + 0.5
            starColor = color(brigthness, brigthness, brigthness)
            if size == 0:
                rend.glPoint(x,y, starColor)
            elif size == 1:
                rend.glPoint(x,y, starColor)
                rend.glPoint(x+1,y, starColor)
                rend.glPoint(x,y+1, starColor)
                rend.glPoint(x+1,y+1, starColor)
            elif size == 2:
                rend.glPoint(x,y, starColor)
                rend.glPoint(x,y+1, starColor)
                rend.glPoint(x+1,y, starColor)
                rend.glPoint(x,y-1, starColor)
                rend.glPoint(x-1,y, starColor)

rend.glFinish("output.bmp")