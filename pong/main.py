# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pos = [1280//2,720//2]
vell =[5,5]
radio = 30
plat_x = 1280//2
plat_largo = 300
izq = False
der = False
plat_vell = 20
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

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

    pos[0]+=vell[0]
    pos[1]+=vell[1]

    if izq:
        plat_x -= plat_vell
    if der:
        plat_x += plat_vell

    if pos[0] <=radio or pos[0] >=screen.size[0]-radio:
        vell[0] *= -1
    if pos[1] <= radio or pos[1] >= screen.size[1]-radio:
        vell[1] *= -1

    if plat_x <= 0:
        plat_x = 0
    if plat_x >= screen.size[0]-plat_largo:
        plat_x = screen.size[0]-plat_largo


    pygame.draw.line(screen,"red",[plat_x,screen.size[1]-50],[plat_largo+plat_x,screen.size[1]-50],30)
    pygame.draw.circle(screen,"blue",pos,radio )
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
