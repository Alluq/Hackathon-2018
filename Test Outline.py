import pygame
import SoundBoardScreen
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()
size = [640, 480]
yeeting=True
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Comic Sans MS", 5)

# You need to rename the .wav files to these simplified versions
soundnamelist = ["Chase.wav", "Classical.wav", "Scary.wav", "Techno.wav", "aliens.wav", "birds.wav", "telephone.wav", "formula1.wav", "shoes.wav", "hyena.wav", "car_engine.wav", "sawingwood.wav", "Spahget.wav", "pristine.wav", "OHI.wav"]
soundlist = []
soundlist.append(pygame.mixer.Sound(soundnamelist[0])) # 1
soundlist.append(pygame.mixer.Sound(soundnamelist[1])) # 2
soundlist.append(pygame.mixer.Sound(soundnamelist[2])) # 3
soundlist.append(pygame.mixer.Sound(soundnamelist[3])) # 4
soundlist.append(pygame.mixer.Sound(soundnamelist[4])) # 5
soundlist.append(pygame.mixer.Sound(soundnamelist[5])) # 6
soundlist.append(pygame.mixer.Sound(soundnamelist[6])) # 7
soundlist.append(pygame.mixer.Sound(soundnamelist[7])) # 8
soundlist.append(pygame.mixer.Sound(soundnamelist[8])) # 9
soundlist.append(pygame.mixer.Sound(soundnamelist[9])) # 10
soundlist.append(pygame.mixer.Sound(soundnamelist[10])) # 11
soundlist.append(pygame.mixer.Sound(soundnamelist[11])) # 12
soundlist.append(pygame.mixer.Sound(soundnamelist[12])) # 13
soundlist.append(pygame.mixer.Sound(soundnamelist[13])) # 14
soundlist.append(pygame.mixer.Sound(soundnamelist[14])) # 15

gae = SoundBoardScreen.Sound_Board(size, screen, soundnamelist)

while yeeting:
    if gae.get_clicked() != None:
        print(gae.get_clicked())
        print("help", soundlist[gae.get_clicked()])
        pygame.mixer.Sound.play(soundlist[gae.get_clicked()])
    screen.fill([255, 255, 255])
    gae.update()
    if gae.get_clicked() != None:
        print(gae.get_clicked())
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            yeeting=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            pass
    if not yeeting:
        break
