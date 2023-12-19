import pygame

def recolectar_nombre():
    pygame.init()
    ventana = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Ingresa tu nombre")

    nombre = ""
    font = pygame.font.Font(None, 36)
    input_rect = pygame.Rect(150, 50, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False

    clock = pygame.time.Clock()

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
                        nombre += event.unicode

        ventana.fill((30, 30, 30))
        txt_surface = font.render(nombre, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_rect.w = width
        ventana.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(ventana, color, input_rect, 2)

        pygame.display.flip()
        clock.tick(30)

