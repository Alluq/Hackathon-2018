import pygame
import time

pygame.init()
pygame.font.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
main = True

timefont = pygame.font.SysFont("Comic Sans MS", 25)

while main:
    screen.fill([255, 255, 255])
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()

