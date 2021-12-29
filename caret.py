import pygame


class Caret:
    def __init__(self,x,y,font_size,color=(255,255,255),thickness = 2):
        self.x = x
        self.y = y
        self.color = color
        self.thick = thickness
        self.font_size = font_size
        self.rect = (x,y,thickness ,font_size)
        self.color_counter = 0
        self.typing_counter = 0
    def change_location(self,x,y):
        self.x = x
        self.y = y
        self.rect = (self.x,self.y,self.thick,self.font_size)
    def draw(self,win,color_list,typing = 0):
        pygame.draw.rect(win,self.caret_blinking(color_list,typing = typing),self.rect)
    def caret_blinking(self,color_list,typing = 0):
        if typing == 0:
            self.color_counter += 1
            if self.color_counter > 66:
                self.color_counter = 1
            if self.color_counter < 33:
                return color_list[0]
            else:
                return color_list[1]
        else:
            return color_list[0]
    def caret_typing_counter(self):
        if self.typing_counter < 75:
            self.typing_counter += 1
        else:
            return 1






