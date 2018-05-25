import pygame
import SoundBoardScreen
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
main = True

timefont = pygame.font.SysFont("Comic Sans MS", 25)

gae = SoundBoardScreen.Sound_Board(size, screen)  # initialize

def soundload():
    soundlist = []
    soundlist.append(pygame.mixer.music.load("Chase.mp3")) # 1
    soundlist.append(pygame.mixer.music.load("Classical.mp3")) # 2
    soundlist.append(pygame.mixer.music.load("Scary.mp3")) # 3
    soundlist.append(pygame.mixer.music.load("Techno.mp3")) # 4
    soundlist.append(pygame.mixer.Sound("alien-spaceship_daniel_simion.wav")) # 5
    soundlist.append(pygame.mixer.Sound("cartoon-birds-2_daniel-simion.wav")) # 6
    soundlist.append(pygame.mixer.Sound("cartoon-telephone_daniel_simion.wav")) # 7
    soundlist.append(pygame.mixer.Sound("formula-1-daniel_simon.wav")) # 8
    soundlist.append(pygame.mixer.Sound("hard_shoes_1-daniel_simon.wav")) # 9
    soundlist.append(pygame.mixer.Sound("hyena-laugh_daniel-simion.wav")) # 10
    soundlist.append(pygame.mixer.Sound("old-car-engine_daniel_simion.wav")) # 11
    soundlist.append(pygame.mixer.Sound("sawing-wood-daniel_simon.wav")) # 12
    return soundlist

sounds = soundload()

while main:
    screen.fill([255, 255, 255])
    gae.update()  # This draws the buttons
    try:
        playing = True
        if playing:
            pygame.mixer.Sound.play(sounds[gae.get_clicked()])
        print("yep",pygame.mixer.Sound.get_length(sounds[gae.get_clicked()]), gae.get_clicked)
    except:
        print("nope")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()

