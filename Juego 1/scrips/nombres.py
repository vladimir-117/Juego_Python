import pygame

def recolectar_nombre():
    pygame.init()
    #creamos al ventana para escribir el nombre del usuario
    ventana = pygame.display.set_mode((400, 200))
    #sirve para dar nombre a la ventana
    pygame.display.set_caption("Ingresa tu nombre")

    
    #Iniciamos la variable nombre con un vacio para ser escrita despues
    nombre = ""
    fuente = pygame.font.Font(None, 36)
    input_rect = pygame.Rect(100, 70, 140, 32) #ubicacion del rectangulo
    nombre_texto = fuente.render("Ingrese nombre del Piloto", True , (255,255,255)) #texto sobre el rectangulo
    color_inactive = pygame.Color('lightskyblue3') # colores de las letras sin escribir
    color_active = pygame.Color('dodgerblue2') #colotes de la letras escritas
    color = color_inactive 
    active = False
    #se encarga de establecer los fotogramas del juego (fps)
    fps = pygame.time.Clock()
    #cremao el bucel principla del funcionamiento del modulo de recolección de nombres
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Salir del juego
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        return nombre  # Devolver el nombre ingresado
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                         # Añadir el carácter solo si no se ha alcanzado la longitud máxima
                        if len(nombre) < 9:
                            nombre += event.unicode
                        

        #crea el fondo del juego
        ventana.fill((30, 30, 30))
        ventana.blit(nombre_texto, (ventana.get_width() // 2 - nombre_texto.get_width() // 2, 10))# se encarga de escribir el texto toma valores de la ventana y el texto a escribir
        txt_surface = fuente.render(nombre, True, color)
        maximo_escritura = max(200, txt_surface.get_width() + 10) # define la loguitud del texto lo  maximo
        input_rect.w = maximo_escritura #Ajusta el ancho de la caja de entrada según la longitud máxima del texto.
        ventana.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5)) #Dibuja el texto ingresado en la caja de entrada.
        pygame.draw.rect(ventana, color, input_rect, 2) # Dibuja el borde de la caja de entrada.

        pygame.display.flip()
        fps.tick(30)

