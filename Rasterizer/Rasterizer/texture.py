import struct

# Texturas de 24 bits
class Texture(object):
    def __init__(self, filename):
        # Se carga la informacion de la imagen, asumiendo
        # que tiene un formato BMP de 24 bits.
        with open(filename, "rb") as image:
            # Tamano del header
            image.seek(10)
            headerSize = struct.unpack('=l' , image.read(4))[0]

            # Tamano de textura
            image.seek(18)
            self.width = struct.unpack('=l' , image.read(4))[0]
            self.height = struct.unpack('=l' , image.read(4))[0]

            # Lectura de tabla de colores
            image.seek(headerSize)
            
            self.pixels = []

            for y in range(self.height):
                pixelRow = []
                for x in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255
                    pixelRow.append([r,g,b])

                self.pixels.append(pixelRow)


    def getColor(self, u, v):
        # Se regresa el valor del pixel si los valores de las uv
        # estan entre 0 y 1.
        if 0<=u<1 and 0<=v<1:
            return self.pixels[int(v * self.height)][int(u * self.width)]
        else:
            return None