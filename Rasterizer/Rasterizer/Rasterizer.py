from gl import Renderer, color

width = 1920
height = 1080

rend = Renderer(width,height)

rend.glClearColor(0.5, 0.5, 0.5)
rend.glClear()

rend.glColor(1,1,1)
rend.glPoint(250,250)

rend.glFinish("output.bmp")