import random
import pygame

from pygame.locals import (
    RLEACCEL
)

# crea las dimenciones de la pantalla 
pantalla_largo = 800
pantalla_alto = 600

#se encarga de redimencionar la imagen con los parametros que se encargan 
ruta_imagen = "assets/nube.png"
ancho_deseado = 300
alto_deseado = 300
imagen_original = pygame.image.load(ruta_imagen)
imagen_redimensionada = pygame.transform.scale(imagen_original, (ancho_deseado, alto_deseado))

class Nube (pygame.sprite.Sprite):
    def __init__(self):
        super (Nube, self). __init__()
        self.surf = pygame.transform.rotate(imagen_redimensionada,0 )
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
       
        self.rect = self.surf.get_rect(

            center=(
                random.randint(pantalla_largo + 20, pantalla_largo + 100),
                random.randint(0, pantalla_alto),

            )
        )
        
          
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
        

    