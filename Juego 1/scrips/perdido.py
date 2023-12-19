import pygame
import sys


def game_over():
    pygame.init()
    from menus.juego import iniciar_juego
    from scrips.nombres import recolectar_nombre
    from menus.menu import menu 
    # Definir el tamaño de la pantalla
    pantalla_largo = 800
    pantalla_alto = 600
    pantalla_juego = pygame.display.set_mode((pantalla_largo, pantalla_alto))

    # Definir el color de fondo
    fondo_color = (0, 0, 0)

    # Definir la fuente y el tamaño del texto
    fuente = pygame.font.Font(None, 36)

    # Creamos el texto de Game Over
    blanco = (255, 255, 255)
    game_over_texto = fuente.render("Game Over", True, blanco)

    # Creamos el texto de Volver a Jugar
    play_again_texto = fuente.render("Presiona R para volver a jugar", True, blanco)

    #Creamos el texto de ir a menu
    menu_texto = fuente.render("Presione esc para ir a menu de inicio",True,blanco)
    # Bucle principal del juego
    while True:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reiniciar el juego
                    nombre_jugador = recolectar_nombre()
                    iniciar_juego(nombre_jugador)
                elif event.key == pygame.K_ESCAPE:
                    menu()
        
    # Menú principal
        pantalla_juego.fill(fondo_color)
        pantalla_juego.blit(game_over_texto, (pantalla_largo // 2 - game_over_texto.get_width() // 2, 200))
        pantalla_juego.blit(play_again_texto, (pantalla_largo // 2 - play_again_texto.get_width() // 2, 300))
        pantalla_juego.blit(menu_texto, (pantalla_largo // 2 - play_again_texto.get_width() // 2, 350))
        pygame.display.flip()
    
    pygame.quit()
