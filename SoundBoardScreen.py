import utility
import random

class Sound_Board:
    def __init__(self, screenSize, screen):
        self.screen = screen
        self.screenSize = screenSize
        self.buttons = []
        for i in range(3):
            for j in range(5):
                self.buttons.append(utility.Button(self.screen,(i*self.screenSize[0]/5,j*screenSize[1]/5,self.screenSize[0]/5,self.screenSize[1]/5),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),Text(self.screen,0,0,"Woah",pygame.font.SysFont("Comic Sans MS",25),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))))
    def update(self):
        for i in self.buttons:
            i.draw()
