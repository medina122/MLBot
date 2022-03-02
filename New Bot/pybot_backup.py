import pyautogui as bot
from time import sleep
import os

path = os.getcwd()

def image_position(img_name: str, conf: float, await_img: bool):
    image = os.path.join(path, 'src', img_name) + '.png'
    cords = bot.locateOnScreen(image, conf)

    if cords != (None):
        print(cords)
    elif not cords and await_img:
        attempt = 0
        sleep(0.25)
        while not cords:
            attempt += 1
            print(f'Locating {img_name}, attempt: {attempt}')
            sleep(0.25)
            cords =  bot.locateOnScreen(image, conf)
    else: print(f'Not found: {img_name}')    
    return cords
    
def locate_image(img_name, conf=0.8, await_img=False, move=True, click=True):
    
    image = image_position(img_name, conf, await_img)

    try:
        if image != (None): 
            if move: bot.moveTo(image)
            if click: bot.click(image)
    except: 
        print('Actions cannot be completed')
    return image
