# Example file showing a basic pygame "game loop"
import pygame
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cont:int = 0

bola = pygame.Rect(1280//2,720//2,60,60)
plataforma = pygame.Rect(1280//2,screen.size[1]-100,300,30)
bola_vell =[5,5]
plat_vell = 10

izq:bool = False
der:bool = False

font = pygame.font.Font(None,72)
puntos = font.render(f"score: {cont} ", True, "black")
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    print(bola_vell)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        teclas_p = pygame.key.get_pressed()
        if teclas_p[pygame.K_LEFT]:
            izq = True
        if teclas_p[pygame.K_RIGHT]:
            der = True
        teclas_s = pygame.key.get_just_released()
        if teclas_s[pygame.K_LEFT]:
            izq = False
        if teclas_s[pygame.K_RIGHT]:
            der = False



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    if izq:
        plataforma.x -= plat_vell
    if der:
        plataforma.x += plat_vell

    bola.x+=bola_vell[0]
    bola.y+=bola_vell[1]

    if plataforma.colliderect(bola):
        bola_vell[1] *= -1
        cont += 1
        puntos = font.render(f"score: {cont} ", True, "black")


    if bola.x <= 0 or bola.x >=screen.size[0] -bola.width:
        bola_vell[0] *= -1
    if bola.y <= 0 or bola.y >= screen.size[1] -bola.width:
        bola_vell[1] *= -1

    if plataforma.x <= 0:
        plataforma.x = 0
    if plataforma.x >= screen.size[0]-plataforma.width:
        plataforma.x = screen.size[0]-plataforma.width


    pygame.draw.rect(screen,"blue",plataforma)
    pygame.draw.rect(screen,"red",bola)
    screen.blit(puntos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(80)  # limits FPS to 80

pygame.quit()
