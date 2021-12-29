from os import path, listdir,stat
import pygame
from settings import *
from Border import Border

class Sticker:
    def __init__(self,win):
        self.screen = win
        self.running = 1
        self.image_group = pygame.sprite.Group()
        self.pointer_image = pygame.Surface((1, 1))
        self.pointer_rect = self.pointer_image.get_rect()
        self.pointer_sprite = pygame.sprite.Sprite()
        self.pointer_sprite.image = self.pointer_image
        self.pointer_sprite.rect = self.pointer_rect
        self.load()
        self.sticker_selected = None
        self.update()


    def load(self):
        self.stickers = []
        self.folder = path.dirname(__file__)
        Border()
        self.sticker_folder = path.join(self.folder,"bordered_sticker")
        sticker_list = [path.join(self.sticker_folder, img) for img in listdir(self.sticker_folder)]
        sticker_list.sort(key=lambda f: stat(f).st_ctime)
        self.sticker_list_unpathed = [path.basename(img) for img in sticker_list]

        sticker_list = self.sticker_list_unpathed
        print("borederd_sticker_list",sticker_list)

        for i in range(len(sticker_list)):
            sprite =pygame.sprite.Sprite()
            image = path.join(self.sticker_folder,sticker_list[i])
            image = pygame.image.load(image).convert_alpha()
            image = pygame.transform.scale(image,(241,130))
            rect = image.get_rect()
            rect.topleft = (((241+10) * (i % 4)) + 5, 10 + ((130+10) * (i//4)))
            self.stickers.append([image,rect])
            sprite.image = image
            sprite.rect = rect
            self.Yoffset = 0
            if (len(sticker_list)%4) != 0:
                self.sticker_map_height = (((len(sticker_list)//4) + 1) * 140) + (4*((len(sticker_list)//4) + 1))
            else:
                self.sticker_map_height = ((len(sticker_list) // 4) * 140) + (4*(len(sticker_list)//4))
            self.image_group.add(sprite)


    def update(self):
        while self.running:
            ##events
            self.pointer_rect.topleft = pygame.mouse.get_pos()

            if (self.sticker_selected != None):
                self.running = 0

            ##re-draw window
            self.screen.fill((0,0,0))

            ##draw stickers
            ##pointing check
            hit = pygame.sprite.spritecollide(self.pointer_sprite, self.image_group, False)
            if hit:
                self.pointing = 1
            else:
                self.pointing = 0

            if self.events() == 1:
                rect = hit[0].rect
                image_no = 4*((rect.y - self.Yoffset)//140) + (rect.x//251)
                self.sticker_selected = [self.sticker_list_unpathed[image_no]]
                print("sticker_list_unpathed")
                print("sticker_selected_name : ", self.sticker_selected[0]," image_no :",image_no)
            self.Draw_stickers()
            pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if len(self.sticker_folder) > 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.pointing:
                        return 1
                    if event.button == 4:
                        self.Yoffset += 6
                    if event.button == 5:
                        self.Yoffset += -6
                        if self.sticker_map_height > HEIGHT:
                            if self.Yoffset < (HEIGHT - self.sticker_map_height) :
                                self.Yoffset += 6
                        else:
                            self.Yoffset = 0
                    if self.Yoffset > 0:
                        self.Yoffset = 0



            if event.type == pygame.QUIT:
                self.running = 0
                self.sticker_selected = None



    def Draw_stickers(self):
        for i in self.stickers:
            self.screen.blit(i[0],i[1].move(0,self.Yoffset))
            self.Add_Border(i[1][0] - 2, i[1].move(0,self.Yoffset)[1] - 2)
            pos = pygame.mouse.get_pos()

    def Add_Border(self,x,y):
        color_list = (RED,GREEN)
        pos = pygame.mouse.get_pos()
        if (x + 10 < pos[0]< (x + 241) ) and  ( y + 10 < pos[1]< ( y + 130) ):
            pygame.draw.rect(self.screen,color_list[1],(x+4,y+4,241-4,130-4),5,0)
        else:
            pygame.draw.rect(self.screen, color_list[0], (x+4, y+4, 241-4, 130-4), 5,0)

    def settings(self):
        self.border_thickness = 4
        self.image_width,self.image_height = 241, 130





