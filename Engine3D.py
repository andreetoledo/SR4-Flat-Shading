#Andree Toledo 18439    
#Lab 4

from gl import Render
from gl import color


render = Render()

render.load('./sonic.obj', translate=(375, 25, 0), scale = (24, 24, 100))

render.glFinish(filename='output.bmp')