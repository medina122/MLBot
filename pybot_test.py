import pyautogui as bot
from time import sleep
import os, random

path = os.getcwd()
tweens = [bot.easeInElastic, bot.easeInBack, bot.easeInBounce, bot.easeInCirc, bot.easeInCubic, bot.easeInExpo, bot.easeInOutBack, bot.easeOutBack, bot.easeOutCirc, bot.easeOutElastic, bot.easeOutCubic, bot.easeOutQuad, bot.easeOutQuint, bot.easeOutQuart, bot.easeOutBounce]

def image_position(img_name: str, conf: float, check: bool):
    image = os.path.join(path, 'src', img_name) + '.png'
    print(image)
    cords = bot.locateOnScreen(image, confidence=conf)

    if cords != (None):
        print(cords)
    elif not cords and check:
        attempt = 0
        sleep(0.25)
        while not cords:
            attempt += 1
            print(f'Locating {img_name}, attempt: {attempt}')
            sleep(0.5)
            cords =  bot.locateOnScreen(image, confidence=conf)
    else: print(f'Not found: {img_name}')    
    return cords
    
def locate_image(img_name, conf=.8, check=False, move=True, click=True, wait=None, end=None):

    if wait != None: sleep(wait)

    image = image_position(img_name, conf, check)

    try:
        if image != (None): 
            if move: bot.moveTo(image, duration=random.randint(10,30)/100, tween=random.choice(tweens))
            if click: bot.click(image, duration=random.randint(10,30)/100, tween=random.choice(tweens))
    except: 
        print('Actions cannot be completed')
    
    if end != None: sleep(end)
    return image