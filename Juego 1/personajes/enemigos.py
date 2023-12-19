import random
import pygame

from pygame.locals import (
    RLEACCEL
)

# crea las dimenciones de la pantalla 
pantalla_largo = 800
pantalla_alto = 600

#se encarga de redimencionar la imagen con los parametros que se encargan 
ruta_imagen = "assets/misiles.png"
ancho_deseado = 50
alto_deseado = 50
imagen_original = pygame.image.load(ruta_imagen)
imagen_redimensionada = pygame.transform.scale(imagen_original, (ancho_deseado, alto_deseado))

class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        super (Enemigo, self). __init__()
        self.surf = pygame.transform.rotate(imagen_redimensionada, 180)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
       
        self.rect = self.surf.get_rect(

            center=(
                random.randint(pantalla_largo + 20, pantalla_largo + 100),
                random.randint(0, pantalla_alto),

            )
        )
        hitbox_width = 20  # Ancho del hitbox reducido
        hitbox_height = 30  # Alto del hitbox reducido
        self.rect.inflate_ip((hitbox_width - self.rect.width), (hitbox_height - self.rect.height))
        self.tiempo_vida_total = 0    
        self.speed = random.randint(8,12)
        

        
    def update(self):
        self.tiempo_vida_total += 1 / 45.0  
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        

    