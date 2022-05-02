from time import sleep
import pyautogui as bot
import random
import colorama, requests, os, pyperclip
from colorama import Fore
import os

colorama.init()

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
            if click: 
                bot.click(image, duration=random.randint(10,30)/100, tween=random.choice(tweens))
                # Si le agrego esto, me jodera las variables que usan el movimiento relativo
                # bot.moveRel(random.randint(200,1200), random.randint(100,800))

    except: 
        print('Actions cannot be completed')
    
    if end != None: sleep(end)
    return image

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_txt(path, name, copy=False, paste=False):

    # Obtenemos y sobrescribimos la ruta para leer un archivo de texto
    data_txt = os.path.join(path, name)+'.txt'
    
    # Abrimos y leemos el archivo 
    with open(data_txt, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
        if copy:
            
            sleep(0.10)
            pyperclip.copy(content)
        
        if paste:

            sleep(0.10)
            bot.hotkey('ctrl', 'v')
        
        file.close()
        return content 

def crear_txt(path, name, content ):
    
    data = os.path.join(path, name)+'.txt'
    
    with open(data, 'a') as file:
        file.write(content + '\n')   
        file.close()

def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")

def corregir_archivo(path, name, content): 
    
    data = os.path.join(path, name) + '.txt'

    with open(data, 'w') as file:
        file.write(content)
        file.close()


def corregir_archivos(name, content):

    mainfolder = r'/home/owner/Downloads/Telegram Desktop/Faltantes'
    
    for folder in os.listdir(mainfolder):

        if mainfolder.startswith('C:'):

            path = mainfolder + f'\{folder}'  

        else: 
            path = mainfolder + f'/{folder}'  

        corregir_archivo(path, name, content)

def listar_productos(path, report=True, delete=True):

    mainfolder = os.listdir(path)
    
    for folder in mainfolder:

        product = ''

        if folder.endswith('.txt'):
            break
        
        else: 

            if path.startswith('C:'):
                    
                product = path + f'\{folder}'

            else: 
                product = path + f'/{folder}'
            
            content = f"""{read_txt(product, 'titulo')} - {read_txt(product, 'precio')}"""
            crear_txt(path, 'productos', content)
    sleep(0.10)
    
    if report:
        productos = read_txt(path, 'productos')
        telegram_report(productos, '-734368278 ')
        
    if delete:

        if path.startswith('C:'):
            data = path + f'\productos.txt'  

        else: 
            data = path + f'/productos.txt'  

        os.remove(data)