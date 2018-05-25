import pygame

class Text:

    #initialization function
    def init(self, screen, x, y, text, font, color):
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

