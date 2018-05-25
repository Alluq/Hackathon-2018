import utility
import random
import pygame



class Sound_Board:
    def __init__(self, screenSize, screen):
        self.screen = screen
        self.screenSize = screenSize
        self.buttons = []
        for i in range(5):
            for j in range(3):
                self.buttons.append(utility.Button(self.screen,(i*self.screenSize[0]/5,j*screenSize[1]/5,self.screenSize[0]/5,self.screenSize[1]/5),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
                                                   utility.Text(self.screen,0,0,"WOAH",pygame.font.SysFont("comicsansms",25),(255,255,255))))
    def update(self):
        for i in self.buttons:
            i.hoverChange()
            i.draw()
    def get_clicked(self):
        for i in self.buttons:
            if i.clickButton():
                return self.buttons.index(i)

