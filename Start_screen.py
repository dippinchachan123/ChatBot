import pygame
from Setting import *
from caret import *

class Start_Screen:
    def __init__(self,win):
        self.list = []
        self.win = win
        self.running = 1
        self.image = pygame.image.load("download.jpg")
        self.rect = self.image.get_rect()
        self.str_list =[]
        self.typing = 0
        self.caret = Caret((width / 2) - 105, height / 5 + 2,22,thickness = 3)
        self.caret_pos = ((width / 2) - (60), height / 5 + 2,22)

    def main(self):

        while self.running:
            ##re-draw window
            self.win.fill((0,0,0))


            ##Draw
            self.win.blit(self.image,self.rect)

            ##events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if self.typing:
                    if event.type == pygame.KEYDOWN:


                        if event.key == pygame.K_BACKSPACE:
                            try:
                                self.str_list.pop()
                            except:
                                pass
                        else:
                            if not ((event.unicode == '') or (event.unicode == '\r')):
                                self.str_list.append(event.unicode)

                        try:
                            if (len(self.str_list) > 6) or (self.str_list[-1] == ''):
                                self.str_list.pop()
                        except:
                            pass
                        print(self.str_list)
                        if event.key == pygame.K_RETURN:
                            self.running = 0
                            self.Name = self.sum_lines(self.str_list) + " :"



                if event.type == pygame.MOUSEBUTTONDOWN :
                    pos_cursor = pygame.mouse.get_pos()
                    if event.button == 1 and ((width/2) - 111 < pos_cursor[0]< 227 + (width/2) - 114) and ( height/5 < pos_cursor[1]< 35 + (height/5)):
                        self.typing = 1

            self.Draw_Text(self.win, "Enter Name")

            for i in range(len(self.str_list)):
                font = pygame.font.Font("freesansbold.ttf", 22)
                str_obj = font.render(self.sum_lines(self.str_list), True, (255,255,255))
                rect = str_obj.get_rect()
                rect.topleft = ((width / 2) - 60, height / 5 + 2)
                self.caret_pos = rect.topright
                self.win.blit(str_obj, rect)
            self.caret.change_location(self.caret_pos[0], self.caret_pos[1])
            if self.typing:
                self.caret.draw(self.win,[(255,255,255),(255,255,255)],1)


            pygame.display.flip()

    def Draw_Text(self,win,str,color = (255,0,0)):
        pos_cursor = pygame.mouse.get_pos()
        font = pygame.font.Font("freesansbold.ttf", 22)

        if ((width/2) - 111 < pos_cursor[0]< 227 + (width/2) - 114) and ( height/5 < pos_cursor[1]< 35 + (height/5)):
            button_background = pygame.draw.rect(win, (0,255,0), ((width / 2) - 114, height / 5 - 5, 230, 35), 4)
            if not self.typing:
                str_obj = font.render(str, True, (255, 255, 255))
                rect = str_obj.get_rect()
                rect.topleft = ((width / 2) - (rect.width / 2), height / 5 + 2)
                win.blit(str_obj, rect)
        else:
            button_background = pygame.draw.rect(win, color, ((width / 2) - 114, height / 5 - 5, 230, 35), 4)
            if not self.typing:
                str_obj = font.render(str , True, (100,100,100))
                rect = str_obj.get_rect()
                rect.topleft = ((width/2) - (rect.width/2), height/5 + 2)
                win.blit(str_obj, rect)

    def sum_lines(self, str_list):
        sum = ""
        for i in str_list:
            try:
                sum += i
            except:
                pass
        return sum




