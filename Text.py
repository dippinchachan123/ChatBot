import pygame
import numpy as np
from Camera import *
from settings import *
from os import  path,listdir,stat


class Text:
    def __init__(self, start_x, start_y=HEIGHT-100, font_size=20, color=(255, 255, 255)):
        self.msg = ""
        self.start_x = start_x
        self.y = start_y
        self.font_size = font_size
        self.rect = (start_x, start_y, 0, 0)
        self.color = color
        self.recv_snd_msg = []
        self.being_written_msg = []
        self.counter = 0
        self.camera = Camera(WIDTH, 2000)
        self.y_offset = 0
        self.y_map_apparent_height = 0
        self.read_msg = 1
        self.yoffset_apparent = 0
        folder = path.dirname(__file__)
        self.sticker_folder = path.join(folder, "bordered_sticker")
        self.sticker_list = listdir(self.sticker_folder)

    def write(self, str_character, counter, backspace=0):
        if str_character:
            try:
                if backspace == 0:
                    self.being_written_msg[counter].append(str_character)
                else:
                    self.being_written_msg[counter].pop()

            except:
                if (backspace == 0):
                    self.being_written_msg.append([str_character])

    def writen_done(self):
        self.recv_snd_msg.append(self.being_written_msg[-1])

    def sum_lines(self, str_list):
        sum = ""
        for i in str_list:
            try:
                sum += i
            except:
                pass
        return sum
    def update_camera(self,event):
        try:
            self.camera.update(event,self.start_y_list[-1],self.yoffset_apparent)
            self.y_offset = self.camera.update(event,self.start_y_list[-1],self.yoffset_apparent)
        except:
            self.camera.update(event, HEIGHT,self.yoffset_apparent)
            self.y_offset = self.camera.update(event, HEIGHT,self.yoffset_apparent)



    def draw_being_typing(self, win, start_x, start_y=HEIGHT - 100, color=(255, 255, 255)):
        for i in range(len(self.being_written_msg)):
            font = pygame.font.Font("freesansbold.ttf", 22)
            str_obj = font.render(self.sum_lines(self.being_written_msg[i]), True, color)
            self.rect2 = str_obj.get_rect()
            start_x,start_y = 10,HEIGHT - 92
            self.rect2.topleft = (start_x, start_y)
            win.blit(str_obj, self.rect2)

    def draw_recv_snd(self, win, start_x =7, color=(0, 0, 255), player=0,client_name = "client"):
        font_size = 21
        self.start_y_list = [5]
        for i in range(len(self.recv_snd_msg)):
            try:
                if (self.recv_snd_msg[i][1][-1:-4:-1]) == "gpj":
                    self.start_y_list.append(self.start_y_list[-1] + 120)

                else:
                    self.start_y_list.append(self.start_y_list[-1] + 30)
            except:
                self.start_y_list.append(self.start_y_list[-1] + 30)
        self.start_y_list = np.array(self.start_y_list)
        contract_factor = 15
        try:
            self.y_map_apparent_height = self.start_y_list[-1]
        except:
            pass

        if self.y_map_apparent_height > HEIGHT - 115:
            self.yoffset_apparent = -(self.y_map_apparent_height - (HEIGHT-115))
        else:
            self.yoffset_apparent = 0


        for i in range(len(self.recv_snd_msg)):
            font = pygame.font.Font("freesansbold.ttf", font_size)

            if self.recv_snd_msg[i][-1] == player:
                str_obj = font.render("You :", True, color)
                self.rect = str_obj.get_rect()
                self.rect.topleft = (start_x, self.start_y_list[i])
                win.blit(str_obj, self.camera.apply(self.rect,self.yoffset_apparent))

            else:
                str_obj = font.render(client_name.capitalize(), True, (255, 0, 0))
                self.rect = str_obj.get_rect()
                self.rect.topleft = (start_x, self.start_y_list[i])
                win.blit(str_obj, self.camera.apply(self.rect,self.yoffset_apparent))

            self.rect_client_name = self.rect
            try:
                if self.recv_snd_msg[i][1][-1:-4:-1] == "gpj":
                    folder = path.dirname(__file__)
                    self.sticker_folder = path.join(folder, "bordered_sticker")
                    img = self.recv_snd_msg[i][1]
                    img_obj = path.join(self.sticker_folder, img)
                    try:
                        img_obj = pygame.image.load(img_obj).convert_alpha()
                    except:
                        self.sticker_folder = path.join(folder, "Loading_Assets")
                        img_obj = path.join(self.sticker_folder, "loadingSticker.jpg")
                        img_obj = pygame.image.load(img_obj).convert_alpha()
                    img_obj = pygame.transform.scale(img_obj, (140, 100))
                    rect = img_obj.get_rect()
                    self.rect.topleft = (start_x + self.rect_client_name.width + 5, self.start_y_list[i]+4)
                    win.blit(img_obj, self.camera.apply(self.rect,self.yoffset_apparent))

                else:
                    str_obj = font.render(self.sum_lines(self.recv_snd_msg[i][:len(self.recv_snd_msg[i]) - 1]), True,
                                          self.color)
                    self.rect = str_obj.get_rect()
                    self.rect.topleft = (start_x + self.rect_client_name.width + 5, self.start_y_list[i])
                    win.blit(str_obj, self.camera.apply(self.rect,self.yoffset_apparent))
            except:
                str_obj = font.render(self.sum_lines(self.recv_snd_msg[i][:len(self.recv_snd_msg[i]) - 1]), True,
                                      self.color)
                self.rect = str_obj.get_rect()
                self.rect.topleft = (start_x + self.rect_client_name.width + 5, self.start_y_list[i])
                win.blit(str_obj, self.camera.apply(self.rect, self.yoffset_apparent))

