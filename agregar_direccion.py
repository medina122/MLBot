from funciones import locate_image, read_txt, telegram_report
from time import sleep
import random, pyautogui as bot, os, pyperclip

if locate_image('ya_casi_publicas', move=False, click=False):
            locate_image('cargar_direccion', wait=1)

            sleep(2)

            locate_image('elegir', check=True, wait=1)
            bot.press('down', presses=random.randint(1,4))
            bot.press('enter')
            bot.press('tab')
            bot.typewrite(str(random.randint(21,87)), interval=random.randint(5,20)/100)
            bot.press('tab')
            bot.typewrite(str(random.randint(30,55)), interval=random.randint(5,20)/100)
            bot.press('tab')
            bot.typewrite(f"Piso {str(random.randint(1,20))} - Local {str(random.randint(1,150))}", interval=random.randint(5,20)/100)
            bot.press('tab')
            bot.typewrite(f"{str(random.randint(1,300))}", interval=random.randint(5,20)/100)
            bot.press('tab')
            bot.press('down', presses=random.randint(1,20), interval=random.randint(5,20)/100)
            sleep(1)
            bot.press('tab')
            bot.press('down', presses=random.randint(1,25), interval=random.randint(5,20)/100)
            bot.press('tab')
            distritos = ['Chachapoyas', 'Asuncion', 'Balsas', 'Cheto', 'Chiliquin', 'Chuquibamba', 'Cochabamba', 'Cochabamba', 'Granada', 'Huancas', 'La Jalca', 'Llata', 'Lucanas', 'Paijan', 'Pampas', 'Pomacocha', 'San Ignacio', 'San Juan', 'Santiago de Chuco', 'Tambobamba', 'Tingo', 'Tocmo', 'Tumbes', 'Yungay', 'Soloco', 'Sonche', 'La peca', 'Imaza', 'Florida', 'Recta', 'Conila', 'Luya']
            bot.typewrite(f"{str(random.choice(distritos))}", interval=random.randint(5,20)/100)
            locate_image('guardar_direccion', wait=2)
            locate_image('guardar_y_publicar', check=True, wait=2)