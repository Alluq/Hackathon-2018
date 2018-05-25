import pygame
import time

pygame.init()
pygame.font.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
main = True

timefont = pygame.font.SysFont("Comic Sans MS", 25)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
    if not main:
        break

    screen.fill([255, 255, 255])
    print(pygame.time.get_ticks() / 1000)
    pygame.display.update()
