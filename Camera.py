import random as rd
import pygame
import pygame.math
from settings import *

class Camera:
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.rect = pygame.Rect(0,0,width,height)
        self.x = 0
        self.y = 0
        self.yoffset = 0



    def apply(self,entity,apparent_yoffset):
        return entity.move(self.x,self.yoffset + apparent_yoffset)
    def update(self,event,msg_map_height,apparent_yoffset):
        if msg_map_height < HEIGHT:
            self.yoffset = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.yoffset += 8
            if event.button == 5:
                self.yoffset += -8
                if msg_map_height > HEIGHT:
                    if (self.yoffset + apparent_yoffset) < (HEIGHT - 115) - msg_map_height:
                        self.yoffset += 8
                else:
                    self.yoffset = 0
            if (self.yoffset + apparent_yoffset) > 0:
                self.yoffset += -8

        return self.yoffset





