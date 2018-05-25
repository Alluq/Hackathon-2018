import pygame

class Text:
    #initialization function
    def __init__(self, screen, x, y, text, font, color):
        self.screen = screen
        self.ojx = float(x)
        self.ojy = float(y)
        self.font = font
        self.text = text
        self.color = color
        self.x = self.ojx
        self.y = self.ojy

    #updates the text and draws it
    def update(self):
        self.screen.blit(self.font.render(str(self.text),True, self.color), (self.x,self.y))

    #centers the text around the x and y point
    def center(self):
        self.x = self.ojx - self.font.size(str(self.text))[0]/2
        self.y = self.ojy - self.font.size(str(self.text))[1]/2

class Button:

    #initialization function
    def __init__(self, screen, rect, color, onColor, label):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.color = [color, onColor, color]
        self.label = label

    #checks if the mouse is in the button area
    def inButton(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    #changes cover is inButton is true
    def hoverChange(self):
        if self.inButton():
            self.color[2] = self.color[1]
        else:
            self.color[2] = self.color[0]

    #check if user has mouse button on pressed when entering the button
    def clickButton(self):
        if pygame.mouse.get_pressed()[0] and self.inButton():
            return True
        else:
            return False

    #draws button with text
    def draw(self):
            pygame.draw.rect(self.screen, self.color[2], self.rect)
            self.label.ojx = self.rect[0] + self.rect[2]/2
            self.label.ojy = self.rect[1] + self.rect[3]/2
            self.label.center()
            self.label.update()

class Slider_Button(Button):
    def slide(self, barX, barW):
        mouseX = pygame.mouse.get_pos()[0]
        if self.clickButton() and mouseX >= barX and mouseX <= barX + barW:
            self.rect[0] = mouseX - self.rect[2]/2
            return True
        else:
            return False
    def draw(self, barX, barW, range):
        self.slide(barX, barW)
        self.label.ojx = barX - 2 * self.label.font.size(str(range))[0]
        self.label.center()
        self.label.update()
        pygame.draw.rect(self.screen, self.color[2], self.rect)

class Slider_Bar:
    def __init__(self,rect, color, centerPoint, screen):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.color = color
        self.centerp = centerPoint
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def center(self):
        self.rect[0] = self.centerp[0] - self.rect[2]/2
        self.rect[1] = self.centerp[1] - self.rect[3] / 2
class Slider:
    def __init__(self, screen, screenSize,pos):
        self.range = 120
        self.val = 0
        self.bar = Slider_Bar((0,0,screenSize[0]*4/5,screenSize[1]/10),(125,125,125),(pos[0],pos[1]),screen)
        self.bar.center()
        self.button = Slider_Button(screen, (self.bar.rect[0],self.bar.rect[1],screenSize[0]/20,screenSize[1]/10),(0,0,0), (125,125,125), Text(screen,self.bar.rect[0],self.bar.rect[1]+self.bar.rect[3]/2,self.val, pygame.font.SysFont("comicsansms",12),(0,0,0)))
    def draw(self):
        self.update()
        self.bar.draw()
        self.button.draw(self.bar.rect[0],self.bar.rect[2], self.range)
    def update(self):
        add = self.bar.rect[2]/self.range
        self.val = (self.button.rect[0] - self.bar.rect[0]) /int(add)
        self.button.label.text = int(self.val)

