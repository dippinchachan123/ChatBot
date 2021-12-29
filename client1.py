import pygame
from caret import Caret
from Text import Text
from Network import Network
from Camera import *
from Setting import*
from Start_screen import *
from Stickers import Sticker
from Border import Border
from Add_Sticker import browser
import os
pygame.init()


win = pygame.display.set_mode((width, height))
str_data = ""

txt_list = []
running = 1

pygame.key.set_repeat(500,80)


def redrawwindow(r=0, g=0, b=0):
    win.fill((r, g, b))

def draw_rect(x,y,width,height,color):
    image = pygame.Surface((width,height))
    rect = image.get_rect()
    image.fill(color)
    rect.topleft = x,y
    return (image,rect)

def type_button(win,color_key,list_being_typing,width_limit):
    color = [(255,0,0),(0,255,0)]
    color_2 = [(100,100,100),(255,255,255)]

    if width_limit > width - 300:
        button_background = pygame.draw.rect(win,color[color_key], (3, HEIGHT- 95, width_limit + 10, 30), 5)
    else:
        button_background = pygame.draw.rect(win, color[color_key], (3, HEIGHT - 95, width - 300, 30), 5)
    font = pygame.font.Font("freesansbold.ttf",22)
    try:
        if len(list_being_typing[0])>0:
            pass
        else:
            str_obj = font.render("Type the Message", True, color_2[color_key])
            rect = str_obj.get_rect()
            rect.topleft = (10, HEIGHT - 92)
            win.blit(str_obj, rect)
    except:
        str_obj = font.render("Type the Message", True, color_2[color_key])
        rect = str_obj.get_rect()
        rect.topleft = (10, HEIGHT - 92)
        win.blit(str_obj, rect)

def Sticker_button(win,color_key):
    color = [(255,0,0),(0,255,0)]
    color_2 = [(100,100,100),(255,255,255)]

    button_background = pygame.draw.rect(win,color[color_key], (10, HEIGHT - 48, 110, 32), 5)

    font = pygame.font.Font("freesansbold.ttf",22)

    str_obj = font.render("Stickers", True, color_2[color_key])
    rect = str_obj.get_rect()
    rect.topleft = (18, HEIGHT - 42)
    win.blit(str_obj, rect)


def Add_Sticker_button(win,color_key):
    color = [(255,0,0),(0,255,0)]
    color_2 = [(100,100,100),(255,255,255)]

    button_background = pygame.draw.rect(win,color[color_key], (135, HEIGHT - 48, 147, 32), 5)

    font = pygame.font.Font("freesansbold.ttf",22)

    str_obj = font.render("AddStickers", True, color_2[color_key])
    rect = str_obj.get_rect()
    rect.topleft = (18 + 125, HEIGHT - 42)
    win.blit(str_obj, rect)

def Clear_Chat(win,color_key):
    color = [(255,0,0),(0,255,0)]
    color_2 = [(100,100,100),(255,255,255)]

    button_background = pygame.draw.rect(win,color[color_key], (282+15, HEIGHT - 48, 130, 32), 5)

    font = pygame.font.Font("freesansbold.ttf",22)

    str_obj = font.render("ClearChat", True, color_2[color_key])
    rect = str_obj.get_rect()
    rect.topleft = (18 + 125 + (282+ 15 - 135), HEIGHT - 42)
    win.blit(str_obj, rect)





def Dlt_stickers():
    folder = os.path.dirname(__file__)
    sticker_folder = os.path.join(folder, "bordered_sticker")
    for img in os.listdir(sticker_folder):
        os.remove(os.path.join(sticker_folder,img))


def main():
    run = True
    global str_data


    ##bordered_sticker_initialisation

    folder = os.path.dirname(__file__)
    sticker_folder_real = os.path.join(folder, "Stickers")
    Sound_folder = os.path.join(folder, "Sound")
    sticker_list = os.listdir(sticker_folder_real)

    Border(sticker_list)
    print("Bordered stickers initialized")

    ###################################
    ##sounds

    ####background Image and text hider

    image_backgr = pygame.image.load("projectr_walpaper_1.jpg")
    image_text_hider = pygame.image.load("projectr_walpaper_1 - Copy.jpg")
    rect_backgr = image_backgr.get_rect()
    rect_backgr_text_hider_copy = image_backgr.get_rect()
    rect_backgr_text_hider_copy.topleft = 0,HEIGHT - 110

    ####################################
    clock = pygame.time.Clock()


    x_start = 2

    counter_writing = 0

    #Text_object_beta
    text = Text(x_start)

    x_caret = 10
    y_caret = height - 92

    caret = Caret(x_start, text.y, 20)
    color_caret = [(255, 255, 255), (0, 0, 0)]
    typing = 1

    text_shadow = Text(x_start, color=(80, 80, 80), font_size=18)
    text_shadow.being_written_msg.append(["type a message"])

    start_screen_obj = Start_Screen(win)
    start_screen_obj.main()


    ##text_obj_final
    n = Network()
    text = n.get_p()[0]
    player_no = n.get_p()[1]
    client_name = "Client"

    pointing = 0
    pointing_2 = 0

    ##line counter
    line_count = 0

    recv_snd_msg = []

    while run:

        clock.tick(60)

        #start_screen()


        try:
            data = n.send((recv_snd_msg, start_screen_obj.Name))
            recv_snd_msg = data[0]
        except:
            data = n.send((text.recv_snd_msg, start_screen_obj.Name))
        try:
            text.recv_snd_msg = data[0][line_count::]
        except:
            text.recv_snd_msg = []
        client_name = data[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                Dlt_stickers()
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 2:
                    print("mouse position : ",pygame.mouse.get_pos())
            if (event.type == pygame.MOUSEBUTTONDOWN) and pointing:
                if event.button == 1:
                    typing = 0
            elif (event.type == pygame.MOUSEBUTTONDOWN) and not pointing:
                if event.button == 1:
                    typing = 1

            if (event.type == pygame.MOUSEBUTTONDOWN) and pointing_2:
                if event.button == 1:
                    obj = Sticker(win)
                    print(id(obj))
                    if obj.sticker_selected != None :
                        recv_snd_msg.append([""] + obj.sticker_selected )
                        try:
                            data = n.send((recv_snd_msg, start_screen_obj.Name))
                            recv_snd_msg = data[0]
                        except:
                            data = n.send((text.recv_snd_msg, start_screen_obj.Name))
                        #text.recv_snd_msg = n.send((text.recv_snd_msg, start_screen_obj.Name))[0]
                        try:
                            text.recv_snd_msg = data[0][line_count::]
                            print("recv_snd_msg", text.recv_snd_msg)
                        except:
                            text.recv_snd_msg = []


            if (event.type == pygame.MOUSEBUTTONDOWN) and pointing_4:
                line_count += len(text.recv_snd_msg)

                text.recv_snd_msg = []

            if (event.type == pygame.MOUSEBUTTONDOWN) and pointing_3:
                if event.button == 1:
                    browser()



            if event.type == pygame.KEYDOWN :

                if (typing % 2 == 0):
                    caret.typing_counter = 0
                    print(event.unicode)
                    if not ((event.unicode == '') or (event.unicode == '\r')):

                        text.write(event.unicode, counter_writing)
                    if event.key == pygame.K_BACKSPACE:
                        text.write("deleting", counter_writing, 1)
                        text.write("deleting", counter_writing, 1)
                    try:
                        print(text.being_written_msg[-1])
                    except:
                        pass
                    if event.key == pygame.K_RETURN:
                        try:
                            if text.being_written_msg[-1][-1]:


                                recv_snd_msg.append([""] + text.being_written_msg[-1])
                                try:
                                    data = n.send((recv_snd_msg, start_screen_obj.Name))
                                    recv_snd_msg = data[0]
                                except:
                                    data = n.send((text.recv_snd_msg, start_screen_obj.Name))
                                # text.recv_snd_msg = n.send((text.recv_snd_msg, start_screen_obj.Name))[0]
                                try:
                                    text.recv_snd_msg = data[0][line_count::]
                                    print("recv_snd_msg", text.recv_snd_msg)
                                except:
                                    text.recv_snd_msg = []
                            text.being_written_msg[0].clear()


                        except:
                            pass
            text.update_camera(event)

        if x_caret > WIDTH - 130:
            try:
                if text.being_written_msg[-1][-1]:
                    recv_snd_msg.append([""] + text.being_written_msg[-1])
                    try:
                        data = n.send((recv_snd_msg, start_screen_obj.Name))
                        recv_snd_msg = data[0]
                    except:
                        data = n.send((text.recv_snd_msg, start_screen_obj.Name))
                    # text.recv_snd_msg = n.send((text.recv_snd_msg, start_screen_obj.Name))[0]
                    try:
                        text.recv_snd_msg = data[0][line_count::]
                        print("recv_snd_msg", text.recv_snd_msg)
                    except:
                        text.recv_snd_msg = []
                text.being_written_msg[0].clear()

            except:
                pass
        ##draw
        ##redraw window

        redrawwindow()
        win.blit(image_backgr,rect_backgr)

        ##draw captions
        pygame.display.set_caption("pygame - " + start_screen_obj.Name[0:len(start_screen_obj.Name)-1])

        ##draw_replies
        text.draw_recv_snd(win, player = player_no, client_name = client_name)
        win.blit(image_text_hider, rect_backgr_text_hider_copy)
        pygame.draw.rect(win, GREY, (0, HEIGHT - 110, 705 , 2))
        #pygame.draw.line(win,WHITE,(705, 390),(824, 497),2)
        text.draw_being_typing(win, x_start)
        if (typing % 2 == 0):



            try:

                x_caret, y_caret = text.rect2.right,HEIGHT - 92
                caret.caret_typing_counter()

            except:
                pass
            caret.change_location(x_caret, y_caret)
            if caret.caret_typing_counter():
                caret.draw(win, color_caret)
            else:
                caret.draw(win, color_caret, 1)



        ##draw typing columnds

        ##button

        pos = pygame.mouse.get_pos()
        if x_caret < width - 310:
            if (6 < pos[0] < width - 310) and  HEIGHT - 93 < pos[1] < (HEIGHT - 76):
                pointing = 1

            else:
                pointing = 0
        else:
            if (6 < pos[0] < x_caret + 10) and HEIGHT - 93 < pos[1] < (HEIGHT - 76):
                pointing = 1

            else:
                pointing = 0

        if pointing or (typing%2 == 0):
            type_button(win, 1, text.being_written_msg, x_caret)
        else:
            type_button(win, 0, text.being_written_msg, x_caret)




        if (10 < pos[0] < 120) and  HEIGHT - 45 < pos[1] < (HEIGHT - 15):
            Sticker_button(win,1)
            pointing_2 = 1
        else:
            Sticker_button(win, 0)
            pointing_2 = 0

        if (135 < pos[0] < 270) and  HEIGHT - 45 < pos[1] < (HEIGHT - 15):
            Add_Sticker_button(win,1)
            pointing_3 = 1
        else:
            Add_Sticker_button(win, 0)
            pointing_3 = 0

        if  (282 + 15) < pos[0] < (282 + 15) + (270-135) and  HEIGHT - 45 < pos[1] < (HEIGHT - 15):
            Clear_Chat(win,1)
            pointing_4 = 1
        else:
            Clear_Chat(win,0)
            pointing_4 = 0





        pygame.display.flip()


main()
Dlt_stickers()

