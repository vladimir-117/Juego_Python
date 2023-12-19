import pygame
from pygame.locals import (
    RLEACCEL
)

#se encarga de redimencionar la imagen con los parametros que se encargan 
ruta_imagen = "assets/nave.png"
ancho_deseado = 80
alto_deseado = 100
imagen_original = pygame.image.load(ruta_imagen)
imagen_redimensionada = pygame.transform.scale(imagen_original, (ancho_deseado, alto_deseado))


#Crea la clase y sus parametros

class Player(pygame.sprite.Sprite):  
    def __init__(self):  
        super(Player,self).__init__()  

        #self.surf = pygame.image.load("imagen_redimensionada").convert()
        self.surf = pygame.transform.rotate(imagen_redimensionada, -90)
        #coloca color al objeto
        self.surf.set_colorkey((255, 225, 225),RLEACCEL)
        # Da atributos al objeto
        self.rect = self.surf.get_rect()
        self.tiempo_vida_total = 0
    
        hitbox_width = 50  # Ancho del hitbox reducido
        hitbox_height = 50  # Alto del hitbox reducido
        #self.rect.inflate_ip((hitbox_width - self.rect.width), (hitbox_height - self.rect.height))
        # Define el hitbox y ajusta su posición para que esté centrado
        self.hitbox = pygame.Rect(0, 0, hitbox_width, hitbox_height)
        self.hitbox.center = self.rect.center
        
    #actualiza la posicion dependiendo el objeto
    def update(self,pressed_keys):

        velocidad = 7
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0 , -velocidad)
        if pressed_keys[pygame.K_DOWN]:    
            self.rect.move_ip(0 , velocidad)
        if pressed_keys[pygame.K_RIGHT]:    
            self.rect.move_ip(velocidad , 0)
        if pressed_keys[pygame.K_LEFT]:    
            self.rect.move_ip(-velocidad , 0)  
        self.tiempo_vida_total += 1 / 45.0  

        self.hitbox.center = self.rect.center
    

    def mostrar_tiempo_vida(self, pantalla):
        font = pygame.font.Font(None, 36)
        tiempo_texto = font.render(f"Tiempo de Vida: {int(self.tiempo_vida_total)} segundos", True, (0, 0, 0))
        pantalla.blit(tiempo_texto, (10, 10))    
        

#DEFINE LOS LIMITES DE MOVIMIENTO
        pantalla_largo = 800
        pantalla_alto = 600

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > pantalla_largo:
            self.rect.right = pantalla_largo
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= pantalla_alto:
            self.rect.bottom = pantalla_alto