import pyautogui as bot, os, pyperclip
from time import sleep
from funciones import locate_image, read_txt, telegram_report

def post(path):

    locate_image('vender', check=True, wait=1)
    locate_image('productos', check=True, wait=2)
    locate_image('productos')
    locate_image('indicaproducto', move=False, click=False, check=True, wait=1)
    locate_image('titulo', move=False, click=False)
    read_txt(path, 'titulo', copy=True, paste=True)
    sleep(2)
    bot.press('enter')

    locate_image('elegircategoria', move=False, click=False, check=True)
    bot.press('enter')
    locate_image('confirmarcategoria', move=False, click=False, check=True, wait=2)
    locate_image('confirmar')

    locate_image('completainformacion', move=False, click=False, check=True, wait=2)
    if locate_image('marca'):
        read_txt(path, 'marca', copy=True, paste=True)
        locate_image('datosproducto')

    if locate_image('modelo'):
        read_txt(path, 'modelo', copy=True, paste=True)
        locate_image('datosproducto')
    locate_image('confirmar', wait=1)
    sleep(1)

    while True:

        # Ubicamos por apartados

        if locate_image('condicion', move=False, click=False):
            locate_image('nuevo', check=True, wait=1)
            sleep(2)
            continue

        elif locate_image('color', move=False, click=False):

            if locate_image('elegircolor'):
                locate_image('color', click=False)
                locate_image('elegirnegro') or bot.typewrite('Negro')
                bot.typewrite(' ')
                read_txt(path, 'telefono', copy=True, paste=True)
                sleep(0.5)
                locate_image('confirmar', wait=2)
                sleep(2)

        elif locate_image('panelfotos', move=False, click=False) and locate_image('portada', move=False, click=False)==False:
            locate_image('fotos')
            sleep(1)
            pyperclip.copy(path+'/img')
            bot.hotkey('ctrl', 'l')
            sleep(0.5)
            bot.hotkey('ctrl', 'v')
            sleep(0.3)
            bot.press('enter')
            sleep(1)
            locate_image('organizar')
            sleep(0.5)
            locate_image('seleccionar')
            sleep(0.8)
            bot.press('enter')
            locate_image('fotos', move=False, click=False, check=True, wait=3)
            locate_image('cantidad')
            bot.press('backspace')
            read_txt(path, 'cantidad', copy=True, paste=True)
            locate_image('confirmar', wait=1)
            sleep(1.5)
            continue

        elif locate_image('codigouniversal', move=False, click=False):
            if locate_image('codigo', wait=1):
                read_txt(path, 'serial', copy=True, paste=True)
            locate_image('continuar', wait=1)
            sleep(1)
            continue

        elif locate_image('fichatecnica', move=False, click=False):

            checklist = ['input', 'input2', 'input3', 'input4', 'input5']

            for input in checklist:
                while True:
                    if locate_image(input, move=True, click=False, co=0.99, duration=0):
                        locate_image('noaplica', move=True, click=True, duration=0)
                        bot.scroll(-30)
                        locate_image('datosproducto', move=True, click=True, duration=0)
                        continue
                    else: break
            sleep(0.25)
            bot.scroll(-1000)
            sleep(1.25)
            for input in checklist:
                while True:
                    if locate_image(input, move=True, click=False, co=0.99, duration=0):
                        locate_image('noaplica', move=True, click=True, duration=0)
                        bot.scroll(-30)
                        locate_image('datosproducto', move=True, click=True, duration=0)
                        continue
                    else: break
            bot.scroll(-1000)
            locate_image('confirmar', wait=3)
            bot.scroll(-1000)
            locate_image('siguiente', check= True, wait=2)
            sleep(1)
            continue

        elif locate_image('soles', move=False, click=False):
            if locate_image('precio', move=False, click=False, wait=1) or locate_image('precio2'):
                read_txt(path, 'precio', copy=True, paste=True)
                locate_image('confirmar', wait=2)
                sleep(1)
            continue

        elif locate_image('tipopublicacion', move=False, click=False):
            if locate_image('premium', wait=1):
                locate_image('confirmar', wait=2)
            sleep(1)
            continue
        
        elif locate_image('mercadoenvios', move=False, click=False):
            locate_image('confirmar', wait=1)    
            sleep(1)
            continue

        elif locate_image('ofrecesretiro', move=False, click=False):
            locate_image('retiro', wait=2)
            sleep(1)
            continue

        elif locate_image('mercadopago', move=False, click=False):
            locate_image('continuar', wait=2)
            sleep(1)
            continue

        elif locate_image('ofrecesgarantia', move=False, click=False) and locate_image('garantia_check', move=False, click=False)==False:
            locate_image('garantia')
            read_txt(path, 'garantia', copy=True, paste=True)            
            locate_image('confirmar', wait=2)   
            sleep(1)
            continue

        elif locate_image('descripcion', move=False, click=False) and locate_image('descripcion2', move=False, click=False)==False:
            locate_image('descripcion', wait=1)

            if locate_image('descripcion2', wait=1):
                read_txt(path, 'descripcion', copy=True, paste=True)
                bot.press('enter')
                bot.press('enter')
                read_txt(path, 'plantilla', copy=True, paste=True)
                locate_image('descripcion')
                bot.scroll(-500)
                locate_image('confirmar', wait=2)
                sleep(1)
            bot.scroll(-500)
            
        elif  locate_image('publicar'):
            locate_image('verpublicacion', check=True, wait=2)
            sleep(2)
            bot.hotkey('ctrl', 'l')
            sleep(0.10)
            bot.hotkey('ctrl', 'c')
            sleep(0.10)
            link = pyperclip.paste()
            telegram_report(f'{read_txt(path, "titulo")}\nPrecio: {read_txt(path, "precio")}\nURL: {link}', '-1001781252897') # BOT
            telegram_report(f'{os.environ.get("USERNAME")}', '-1001781252897') # BOT
            break

def post_email():

    if locate_image('profile'):

        profile_location = locate_image('account_mail', move=False, click=False, wait=1)[1]

        bot.moveTo(profile_location[0]+80, profile_location[1]+30)
        sleep(0.20)
        bot.tripleClick(interval=0.02)
        bot.hotkey('ctrl', 'c')
        data = f"Email: {pyperclip.paste()}"
        sleep(1)
        bot.click()
        
        telegram_report(f"{data}", '-1001781252897')

if __name__ == '__main__':

    opcion = input('Ingrese opcion: ')

    if int(opcion) == 1:
        path = input(r'Ingrese carpeta del producto: ')
        post(path)
        post_email()
