import pygame

def iniciar_juego(nombre_jugador):
    #importa los movimientos del personaje desde la libreria 
    from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        )

    pygame.init()

    # crea las dimenciones de la pantalla 
    pantalla_largo = 800
    pantalla_alto = 600


    #crea la pantalla con al dimenciones dadas 
    ventana = pygame.display.set_mode((pantalla_largo, pantalla_alto))

    #crea el evento de enemigos usa un tiempo para crearlos en distinto momentos
    AñadirEnemigo = pygame.USEREVENT + 1
    pygame.time.set_timer(AñadirEnemigo, 250)

    #jugador y enemigo importado desde scrips 
    from personajes.jugador import Player
    from personajes.enemigos import Enemigo
    from scrips.perdido import game_over
    from scrips.records import guardar_record,cargar_record,Record
    
    #creador del jugador 
    player1 = Player()

    #Creador  del evento  enemigos inicial
    enemigos = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)

    #inicia el juego (establece el parametro a jugando para iniciar los otros parametros)
    jugando = True

    #crea la ventana de juego
    while jugando:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # para cerrar el juego con esc 
                if event.key == K_ESCAPE:
                    jugando = False

            elif event.type == QUIT:
                    jugando = False
                    # llama al evento de los enemigos
            elif event.type == AñadirEnemigo:
                # Crea a los enemigos en grupo
                new_enemy = Enemigo()
                enemigos.add(new_enemy)
                all_sprites.add(new_enemy)


        #recibe las teclas de entrada
        teclas_presionadas = pygame.key.get_pressed()


        #actualza los sprites en base a las teclas presionadas 
        player1.update(teclas_presionadas)
        

        # actualiza la posicion de los enemigos 
        enemigos.update()

        #dibujar los enemigos 
        for entity in all_sprites:
            ventana.blit(entity.surf ,entity.rect)

        #Coliciones con el jugador
        if pygame.sprite.spritecollideany(player1,enemigos):
            player1.kill()
            jugando = False
            # Crear un objeto Record
            nuevo_record = Record(nombre_jugador,int(round(float(player1.tiempo_vida_total))))
            guardar_record(nuevo_record)
            

            game_over()
                
        # Rellena la ventana con un color antes de dibujar
        ventana.fill((135, 206, 250))
            
        # Es para todos los ojetos en pantalla para que se re-escribe
        for entity in all_sprites:
            ventana.blit(entity.surf, entity.rect)

        #renderiza al jugador a la posicion del teclado
        ventana.blit(player1.surf,player1.rect)
        player1.mostrar_tiempo_vida(ventana)

        #define los fotogramas por segundo en el juego
        Fps = pygame.time.Clock()
            # Actualiza la pantalla
        pygame.display.flip()

        Fps.tick(50)

    
    pygame.quit()

