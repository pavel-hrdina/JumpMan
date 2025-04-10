import pygame   

pygame.init()

height = 600
width = 600
screen = pygame.display.set_mode((width,height))

lets_con = True

if lets_con:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_con = False

pygame.quit()    