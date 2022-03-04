from pydoc import locate
import pyautogui as bot, os, pyperclip, random
from time import sleep
# from funciones import listar_productos, locate_image, read_txt, telegram_report / antes

# despues
from funciones import read_txt, telegram_report
from pybot_test import locate_image

telefono = '932928977'

plantilla = """
___//_//_//9__3__2___9__2__8___9__7__7///___//__//___

>>>>LEER IMPORTANTE ---- TERMINOS Y CONDICIONES <<<<<

FORMAS DE PAGO Y ENTREGA:
1. Aceptamos todos los medios de pago desde la plataforma de Mercado Pago.
2. Los pagos mediante saldo de Mercado pago o la opción Pago Efectivo de Mercado Pago son de acreditación inmediata.
3. Los pagos con tarjetas están sujetos a verificación. No se aceptan pagos de tarjetas débito o crédito de cuentas nuevas o sin reputación, compras con cuentas con mala reputación serán canceladas.
4. Nuestra tienda es en línea. Se entrega boleta con DNI.
5. Cualquier duda o consulta en la opción de preguntas.
6. Para mas información te dejamos nuestro numero de contacto en el apartado de características principales
"""

def post(path):

    locate_image('vender', check=True, wait=3)

    if locate_image('nueva_publicacion', wait=random.randint(3,5)):
        sleep(random.randint(2,3))
    locate_image('hola_productos', check=True, wait=5)
    bot.moveTo(random.randint(300,500), random.randint(100,800), duration=0.20)
    locate_image('productos', wait=5)
    sleep(0.5)
    locate_image('indicaproducto', move=False, click=False, check=True, wait=5)
    locate_image('titulo', move=False, click=False) or locate_image('titulo2')
    read_txt(path, 'titulo', copy=True, paste=True)
    sleep(2)
    bot.press('enter')
    locate_image('elegircategoria', move=False, click=False, check=True, wait=3)
    bot.press('enter')
    locate_image('confirmarcategoria', move=False, click=False, check=True, wait=2)
    locate_image('confirmar', wait=2)

    locate_image('completainformacion', move=False, click=False, check=True, wait=2)
    
    if locate_image('marca'):
        read_txt(path, 'marca', copy=True, paste=True)
        locate_image('datosproducto', duration=0)

    if locate_image('modelo'):
        read_txt(path, 'modelo', copy=True, paste=True)
        locate_image('datosproducto', duration=0)
    locate_image('confirmar', wait=3)

    sleep(3)

    while True:

        # Ubicamos por apartados

        if locate_image('condicion', move=False, click=False, NotFound=False):
            locate_image('nuevo', check=True, wait=3)
            sleep(random.randint(4,5))
            continue

        elif locate_image('color', move=False, click=False, NotFound=False):

            if locate_image('elegircolor'):
                locate_image('color', click=False)
                locate_image('elegirnegro') or bot.typewrite('Negro')
                sleep(0.20)
                bot.typewrite(' ')
                sleep(0.10)
                bot.typewrite(telefono)
                sleep(1)
                locate_image('confirmar', wait=2)
                sleep(random.randint(4,5))

        elif locate_image('panelfotos', move=False, click=False, NotFound=False) and locate_image('portada', move=False, click=False, NotFound=False)==False:

            if locate_image('fotos') and locate_image('portada', move=False, click=False)==False:
                sleep(2)

                if os.name == 'posix': pyperclip.copy(path+'/img') 
                else:  pyperclip.copy(path+'\img')

                bot.hotkey('ctrl', 'l')
                sleep(0.05)
                bot.press('backspace')
                sleep(0.12)
                bot.hotkey('ctrl', 'v')
                sleep(0.20)
                bot.press('enter')
                sleep(2)

                if os.name == 'posix': 
                    sleep(0.10)
                    bot.hotkey('ctrl', 'a')
                    sleep(0.15)
                    bot.press('enter')

                else: 
                    locate_image('organizar')
                    sleep(0.5)
                    locate_image('seleccionar')
                    sleep(0.8)
                    bot.press('enter')

                locate_image('fotos', move=False, click=False, check=True, wait=3)
                
                bot.scroll(-300)
                sleep(2)
                
                if locate_image('cantidad') or locate_image('cantidad2'):
                    sleep(0.5)
                    bot.hotkey('ctrl', 'a')
                    sleep(0.10)
                    bot.press('backspace')
                    sleep(0.5)
                    bot.typewrite(str(random.randint(3,9)))
                
                locate_image('confirmar', wait=3)
                sleep(3)
            continue

        elif locate_image('codigouniversal', move=False, click=False, NotFound=False):
            if locate_image('codigo', wait=2):
                bot.typewrite('90311017', interval=0.05)
            locate_image('continuar', wait=3)
            sleep(2)
            continue

        elif locate_image('fichatecnica', move=False, click=False, NotFound=False):

            checklist = ['input', 'input2', 'input3', 'input4', 'input5']

            for input in checklist:
                while True:
                    if locate_image(input, move=True, click=False, co=0.99, duration=0):
                        locate_image('noaplica', move=True, click=True, duration=0)
                        bot.scroll(-30)
                        locate_image('datosproducto', move=True, click=True, duration=0)
                        continue
                    else: break
            for input in checklist:
                while True:
                    if locate_image(input, move=True, click=False, co=0.99, duration=0):
                        locate_image('noaplica', move=True, click=True, duration=0)
                        bot.scroll(-30)
                        locate_image('datosproducto', move=True, click=True, duration=0)
                        continue
                    else: break
            sleep(0.2)
            bot.scroll(-800)
            locate_image('confirmar', check= True, wait=3)
            sleep(0.5)
            bot.scroll(-800)
            locate_image('siguiente', check= True, wait=3)
            sleep(2)
            continue

        elif locate_image('ya_casi_publicas', move=False, click=False, NotFound=False):
            locate_image('cargar_direccion', wait=3)

            sleep(2)

            locate_image('elegir', check=True, wait=2)
            bot.press('down', presses=1, interval=0.1)
            bot.press('enter')
            bot.press('tab')
            sleep(0.30)
            bot.typewrite(str(random.randint(21,87)), interval=random.randint(8,20)/100)
            bot.press('tab')
            sleep(0.30)
            bot.typewrite(str(random.randint(30,55)), interval=random.randint(8,20)/100)
            sleep(0.30)
            bot.press('tab')
            bot.typewrite(f"Piso {str(random.randint(1,20))} - Local {str(random.randint(1,150))}", interval=random.randint(8,20)/100)
            sleep(0.30)
            bot.press('tab')
            bot.typewrite(f"{str(random.randint(1,300))}", interval=random.randint(8,20)/100)
            sleep(0.10)
            bot.press('tab')
            bot.press('down', presses=random.randint(1,20), interval=random.randint(8,20)/100)
            sleep(2)
            bot.press('tab')
            bot.press('down', presses=random.randint(1,25), interval=random.randint(8,20)/100)
            sleep(0.30)
            bot.press('tab')
            sleep(0.30)
            distritos = ['Chachapoyas', 'Asuncion', 'Balsas', 'Cheto', 'Chiliquin', 'Chuquibamba', 'Cochabamba', 'Cochabamba', 'Granada', 'Huancas', 'La Jalca', 'Llata', 'Lucanas', 'Paijan', 'Pampas', 'Pomacocha', 'San Ignacio', 'San Juan', 'Santiago de Chuco', 'Tambobamba', 'Tingo', 'Tocmo', 'Tumbes', 'Yungay', 'Soloco', 'Sonche', 'La peca', 'Imaza', 'Florida', 'Recta', 'Conila', 'Luya']
            bot.typewrite(f"{str(random.choice(distritos))}", interval=random.randint(8,20)/100)
            locate_image('guardar_direccion', wait=2)
            locate_image('telefono', wait=2, check=True)
            bot.typewrite('950', interval=0.09)
            sleep(0.20)
            bot.typewrite(str(random.randint(235412,965487)), interval=0.07)
            locate_image('guardar_y_publicar', check=True, wait=4)
        
        elif locate_image('soles', move=False, click=False, NotFound=False):
            if locate_image('precio', move=False, click=False, wait=1) or locate_image('precio2'):
                read_txt(path, 'precio', copy=True, paste=True)
                locate_image('confirmar', wait=3)
                sleep(1)
            continue

        elif locate_image('tipopublicacion', move=False, click=False, NotFound=False):
            if locate_image('premium', wait=1):
                sleep(2)
                bot.scroll(-300)
                locate_image('confirmar', wait=3)
            sleep(1)
            continue
        
        elif locate_image('mercadoenvios', move=False, click=False, NotFound=False):
            locate_image('confirmar', wait=2)    
            sleep(1)
            continue

        elif locate_image('elige_un_domicilio', move=False, click=False, NotFound=False):
            domicilio = locate_image('elige_un_domicilio', wait=3)[1]
            bot.moveTo(domicilio[0]+35, domicilio[1]+130, duration=0.25)
            sleep(2)
            bot.click()
            sleep(2)
            continue

        elif locate_image('ofrecesretiro', move=False, click=False, NotFound=False):
            locate_image('retiro', wait=2)
            sleep(1)
            continue

        elif locate_image('mercadopago', move=False, click=False, NotFound=False):
            locate_image('continuar', wait=2)
            sleep(1)
            continue

        elif locate_image('ofrecesgarantia', move=False, click=False, NotFound=False) and locate_image('garantia_check', move=False, click=False, NotFound=False)==False:
            locate_image('garantia')
            bot.typewrite('12', interval=0.05)           
            locate_image('confirmar', wait=3)   
            sleep(1)
            continue

        elif locate_image('descripcion', move=False, click=False, NotFound=False) and locate_image('descripcion2', move=False, click=False, NotFound=False)==False:
            locate_image('descripcion', wait=1)

            if locate_image('descripcion2', wait=1):
                sleep(0.20)
                bot.typewrite(">>>> CARACTERISTICAS DEL PRODUCTO <<<<<", interval=0.04)
                sleep(0.2)
                bot.press('enter')
                sleep(0.2)
                bot.press('enter')
                sleep(0.3)
                read_txt(path, 'descripcion', copy=True, paste=True)
                sleep(0.20)
                bot.press('enter')
                sleep(0.20)
                bot.press('enter')
                sleep(0.20)
                pyperclip.copy(plantilla)
                bot.hotkey('ctrl', 'v')
                sleep(0.70)
                locate_image('descripcion')
                bot.scroll(-500)
                locate_image('confirmar', wait=2)
                sleep(2)
            bot.scroll(-500)
            sleep(1)
                        
            locate_image('publicar', check=True, wait=2)
            sleep(5)
            bot.scroll(-10)
            locate_image('verpublicacion', check=True, wait=5)
            sleep(3)
            locate_image('soles_producto_publicado', move=False, click=False, check=True)
            bot.hotkey('ctrl', 'l')
            sleep(0.20)
            bot.hotkey('ctrl', 'c')
            sleep(0.20)
            link = pyperclip.paste()
            sleep(0.10)
            telegram_report(f'{read_txt(path, "titulo")}\n{read_txt(path, "precio")} Soles\n{link}', '-1001781252897') # BOT
            break

def post_email():

    if locate_image('profile'):

        profile_location = locate_image('account_mail', move=False, click=False, wait=1)[1]

        bot.moveTo(profile_location[0]+80, profile_location[1]+30)
        sleep(0.20)
        bot.tripleClick(interval=0.02)
        bot.hotkey('ctrl', 'c')
        data = f"{pyperclip.paste()}"
        sleep(1)
        bot.click()
        
        telegram_report(f"{data}", '-734368278 ')