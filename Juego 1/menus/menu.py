import pygame
import sys
from menus.juego import iniciar_juego
from scrips.nombres import recolectar_nombre
from scrips.records import cargar_record


def menu():
    #inicia el pygame
    pygame.init()
    #creador de la ventana
    pantalla_altura = 600
    pantalla_largo = 800
    pantalla_juego = pygame.display.set_mode((pantalla_largo,pantalla_altura))
    pygame.display.set_caption("Mi Juego")

    #colores
    blanco = (255,255,255)
    negro = (0,0,0)

    #fuente de texto 
    fuente = pygame.font.Font(None,36)

    Jugar_texto = fuente.render("Jugar",True,blanco)
    salir_texto = fuente.render("Salir",True,blanco)
    record_texto = fuente.render("Record",True,blanco)
    titulo_texto = fuente.render("Prueba Juego",True,blanco)
    volver_texto = fuente.render("Volver",True,blanco)
    records_jugadores_texto=fuente.render("Mejores record",True,blanco)

    #Ubicacion de los textos
    Jugar_ubicacion = Jugar_texto.get_rect(center=(pantalla_largo // 2 ,pantalla_altura// 2 -50 ))
    salir_ubicacion = salir_texto.get_rect(center=(pantalla_largo // 2, pantalla_altura//2 + 50)) 
    record_ubicacion = record_texto.get_rect(center=(pantalla_largo//2, pantalla_altura // 2 ))
    titulo_ubicacion = titulo_texto.get_rect(center=(pantalla_largo//2, pantalla_altura//2-200 )) 
    volver_ubicacion = volver_texto.get_rect(center=(pantalla_largo//2,pantalla_altura -50))
    records_jugadores_ubicacion = records_jugadores_texto.get_rect(center=(pantalla_largo//2,pantalla_altura//2-200))

    #Bucle del juego 
    corriendo = True
    menu = True 
    mostrar_registros = False
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    corriendo = False
            
            if menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Jugar_ubicacion.collidepoint(event.pos):
                        nombre_jugador = recolectar_nombre()
                        if nombre_jugador:
                            iniciar_juego(nombre_jugador)
                        else:
                            print("El jugador canceló.")
                        
                    elif record_ubicacion.collidepoint(event.pos):
        
                        records = cargar_record() 
                        mostrar_registros = True
                
                    elif volver_ubicacion.collidepoint(event.pos):
                        mostrar_registros = False
                    
                    elif salir_ubicacion.collidepoint(event.pos):
                        corriendo = False
                
        
        if menu:
        #Menu principal
            pantalla_juego.fill(negro)
            pantalla_juego.blit(titulo_texto,titulo_ubicacion)
            pantalla_juego.blit(Jugar_texto,Jugar_ubicacion)
            pantalla_juego.blit(salir_texto,salir_ubicacion)
            pantalla_juego.blit(record_texto,record_ubicacion)

            if mostrar_registros:
                #muestra los registros
                #print("Mostrar")
                pantalla_juego.fill(negro)
                for i, record in enumerate(records): #se ingresa un bucle for para crear una manera de escribir los elemenetos en el cvs
                    nombre_text = fuente.render(record.nombre, True, blanco)
                    puntaje_text = fuente.render(str(record.puntaje), True, blanco)
                    pantalla_juego.blit(nombre_text, (pantalla_largo // 2 - 100, pantalla_altura // 4 + i * 50))
                    pantalla_juego.blit(puntaje_text, (pantalla_largo // 2 + 100, pantalla_altura // 4 + i * 50))
                pantalla_juego.blit(volver_texto, volver_ubicacion)
                pantalla_juego.blit(records_jugadores_texto, records_jugadores_ubicacion)
            
            else:
                pass

        pygame.display.flip()


    pygame.quit()
    sys.exit()