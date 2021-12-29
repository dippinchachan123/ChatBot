from os import path,listdir,stat,remove
from PIL import Image,ImageOps

def Border(sticker_list = 0):
###dont use it ,it will add border to stickers
    folder = path.dirname(__file__)
    sticker_folder = path.join(folder,"Stickers")
    bordered_sticker_folder = path.join(folder,"bordered_sticker")
    sticker_list = [path.join(sticker_folder,img) for img in listdir(sticker_folder)]
    sticker_list.sort( key = lambda f: stat(f).st_ctime)
    print("sticker_lst_real",sticker_list)
    for i in listdir(bordered_sticker_folder):
        print(path.join(bordered_sticker_folder,i))
    '''for i in range(len(sticker_list)):
        try:
            img = Image.open(sticker_list[i])
            img = ImageOps.expand(img,4,(0,255,0))
            img.save(path.join(bordered_sticker_folder,path.basename(sticker_list[i])))
        except:
            pass'''
Border()






