import utility
import random
import pygame



class Sound_Board:
    def __init__(self, screenSize, screen, soundnames):
        self.screen = screen
        self.screenSize = screenSize
        self.buttons = []
        for i in range(5):
            count = 0
            count += i * 3
            for j in range(3):
                count += 1
                self.buttons.append(utility.Button(self.screen,(i*self.screenSize[0]/5,j*screenSize[1]/5,self.screenSize[0]/5,self.screenSize[1]/5),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),#(0+255/(i+2),20,20),(0+255/(j+2),135,0),
                                                   utility.Text(self.screen,0,0,soundnames[count-1],pygame.font.SysFont("comicsansms",15),(255,255,255))))
        self.sliders = [utility.Slider(screen,screenSize, (screenSize[0]/2,screenSize[1]*4/6)),utility.Slider(screen, screenSize, (screenSize[0] / 2, screenSize[1] * 5 / 6))]
    def update(self):
        for i in self.buttons:
            i.hoverChange()
            i.draw()
        for i in self.sliders:
            self.slider.draw()
    def get_clicked(self):
        for i in self.buttons:
            if i.clickButton():
                return self.buttons.index(i)
