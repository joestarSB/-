import pygame
pygame.init()
pygame.display.set_mode((10, 10))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
