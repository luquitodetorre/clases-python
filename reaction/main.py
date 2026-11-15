# Example file showing a basic pygame "game loop"
import pygame
import random


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
input:bool = False
fase:int = 0
milisegundos: int = random.randint(1000,5000)
tiempo_inicio = 0
tiempo_inicio_reacion = 0
msj = "cick izquierdo"
font = pygame.font.Font(None,50)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    input = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            input = True


    if fase == 0:
        screen.fill("cyan")
        if input:
           fase = 1
           msj= "esperar verde"
           tiempo_inicio = pygame.time.get_ticks()
    elif fase == 1:
        screen.fill("red")
        if pygame.time.get_ticks() - tiempo_inicio >= milisegundos:
            fase = 2
            tiempo_inicio_reacion = pygame.time.get_ticks()
            msj = "¡AHORA!"
        elif input:
            fase = 0
            msj = "demasiado pronto"

    elif fase == 2:
        screen.fill("green")
        if input:
            tiempo_reacion =pygame.time.get_ticks() - tiempo_inicio_reacion
            msj = f"{tiempo_reacion}ms"
            fase=0

    # fill the screen with a color to wipe away anything from last frame
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    txt = font.render(msj , True , "black")
    screen.blit(txt)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
