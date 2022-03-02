from pydoc import describe
from time import sleep
import pyautogui as bot
import random
import colorama, requests, os, pyperclip
from colorama import Fore
import os

colorama.init()

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def locate_image(name, move=True, click=True, check=False, co=0.8, wait=0, duration=0.20, NotFound=True):
    
    bot.PAUSE = random.randint(5,20)/100

    if wait != 0: sleep(wait)

    path = os.path.abspath(os.path.dirname(__file__))
    data = ''

    if path.startswith('C:'):
        data = path +f'\src\{name}.png'
    
    else:
        data = path +f'/src/{name}.png'
    
    
    if check:

        while True:
            sleep(0.25)
            cords = bot.locateOnScreen(data, confidence=co)
            
            if cords:

                sleep(0.5)

                if move:
                    bot.moveTo(cords, duration=duration)

                if click:
                    bot.click(cords, duration=duration)
                    sleep(0.20)
                
                print(f'Found {name}')
            
                return True, cords

            else: 
                
                if NotFound:
                    print(f'Not found {name}')

    else:
        
        cords = bot.locateOnScreen(data, confidence=co)

        if cords:

            if move:
                bot.moveTo(cords, duration=duration)

            if click:
                bot.click(cords, duration=duration)
            
            print(f'Found {name}')

            return True, cords
        
        else: 
            print(f'Not found {name}')
            return False

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