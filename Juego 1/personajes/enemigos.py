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

#crea la clase enemigos
class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        super (Enemigo, self). __init__()
        self.surf = pygame.transform.rotate(imagen_redimensionada, 180)#redirecciona la imagen y usa una imagen redimensionada
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
       
        self.rect = self.surf.get_rect(

            center=(
                random.randint(pantalla_largo + 20, pantalla_largo + 100),
                random.randint(0, pantalla_alto),

            )
        )
        #redimencion al hitbox del enemigo
        hitbox_ancho = 10  # Ancho del hitbox reducido
        hitbox_alto = 30  # Alto del hitbox reducido
        self.rect.inflate_ip((hitbox_ancho - self.rect.width), (hitbox_alto - self.rect.height))
        self.tiempo_vida_total = 0    
        self.velocidad = random.randint(8,12)
        

    #define  el movimeinto del misil  
    def update(self):
        #self.tiempo_vida_total += 1 / 45.0  
        self.rect.move_ip(-self.velocidad, 0)
        if self.rect.right < 0:
            self.kill()
        

    
