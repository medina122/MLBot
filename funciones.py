from time import sleep
import pyautogui as bot
import colorama, requests, os, pyperclip
from colorama import Fore

colorama.init()

def locate_image(name, move=True, click=True, check=False, co=0.8, wait=0, duration=0.10):
    
    if wait != 0: sleep(wait)

    path = os.path.abspath(os.path.dirname(__file__))
    data = ''

    if path.startswith('C'):
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
                
                print(f'Found {data}')
            
                return True, cords

            else: 
                print(f'Not found {data}')

    else:
        
        cords = bot.locateOnScreen(data, confidence=co)

        if cords:

            if move:
                bot.moveTo(cords, duration=duration)

            if click:
                bot.click(cords, duration=duration)
            
            print(f'Found {data}')

            return True, cords
        
        else: 
            print(f'Not found {data}')
            return False

def read_txt(path, name, copy=False, paste=False):

    # Obtenemos y sobrescribimos la ruta para leer un archivo de texto
    data_txt = ''

    if path.startswith('C:'):
        data_txt = path + f'\{name}.txt' 

    else: 
        data_txt = path + f'/{name}.txt'  
    
    # Abrimos y leemos el archivo 
    with open(data_txt, 'r', encoding='utf-8') as file:
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
    
    if path.startswith('C:'):
        data = path + f'\{name}.txt'  

    else: 
        data = path + f'/{name}.txt'  
    
    with open(data, 'a') as file:
        file.write(content + '\n')   
        file.close()

def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")
