import pyautogui as pg, os, pyperclip, random
from time import sleep
from Tools.funciones import read_txt, telegram_report
from bot_master import PyAutoGUI_Master

Bot = PyAutoGUI_Master()

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

    Bot.locate('vender', check=True, wait=3)

    if Bot.locate('nueva_publicacion', wait=random.randint(3,5)):
        sleep(random.randint(2,3))
    Bot.locate('hola_productos', check=True, wait=3)
    pg.moveTo(random.randint(300,500), random.randint(100,800), duration=0.20)
    Bot.locate('productos', wait=2)
    sleep(0.5)
    Bot.locate('indicaproducto', move=False, click=False, check=True, wait=3)
    Bot.locate('titulo', move=False, click=False) or Bot.locate('titulo2')
    read_txt(path, 'titulo', copy=True, paste=True)
    sleep(2)
    pg.press('enter')
    Bot.locate('elegircategoria', move=False, click=False, check=True, wait=2)
    pg.press('enter')
    Bot.locate('confirmarcategoria', move=False, click=False, check=True, wait=2)
    Bot.locate('confirmar', wait=2, check=True)

    Bot.locate('completainformacion', move=False, click=False, check=True, wait=2)
    
    if Bot.locate('marca'):
        read_txt(path, 'marca', copy=True, paste=True)
        Bot.locate('datosproducto')

    if Bot.locate('modelo'):
        read_txt(path, 'modelo', copy=True, paste=True)
        Bot.locate('datosproducto')
    Bot.locate('confirmar', wait=2)

    sleep(3)

    while True:

        # Ubicamos por apartados

        if Bot.locate('condicion', move=False, click=False, wait=0.25):
            Bot.locate('nuevo', check=True, wait=2)
            sleep(random.randint(3,4))
            continue

        elif Bot.locate('color', move=False, click=False, wait=0.25):

            if Bot.locate('elegircolor',):
                Bot.locate('color', click=False, move=True)
                Bot.locate('elegircolor2')
                Bot.locate('elegirnegro') or pg.typewrite('Negro')
                sleep(0.20)
                pg.typewrite(' ')
                sleep(0.10)
                pg.typewrite(telefono)
                sleep(1)
                Bot.locate('confirmar', wait=2)
                sleep(random.randint(3,4))

        elif Bot.locate('panelfotos', click=False, wait=0.25) and not Bot.locate('portada', click=False):

            if Bot.locate('panelfotos') and not Bot.locate('portada', click=False):
                sleep(2)

                if os.name == 'posix': pyperclip.copy(path+'/img') 
                else:  pyperclip.copy(path+'\img')

                pg.hotkey('ctrl', 'l')
                sleep(0.05)
                pg.press('backspace')
                sleep(0.12)
                pg.hotkey('ctrl', 'v')
                sleep(0.20)
                pg.press('enter')
                sleep(2)

                if os.name == 'posix': 
                    sleep(0.10)
                    pg.hotkey('ctrl', 'a')
                    sleep(0.15)
                    pg.press('enter')

                else: 
                    Bot.locate('organizar') or Bot.locate('organizar2')
                    sleep(0.5)
                    Bot.locate('seleccionar') or Bot.locate('seleccionar2')
                    sleep(0.5)
                    pg.press('enter')

                Bot.locate('panelfotos', move=False, click=False, check=True, wait=2)
                
                pg.scroll(-300)
                sleep(2)
                
                if Bot.locate('cantidad') or Bot.locate('cantidad2'):
                    sleep(0.5)
                    pg.hotkey('ctrl', 'a')
                    sleep(0.10)
                    pg.press('backspace')
                    sleep(0.5)
                    pg.typewrite(str(random.randint(3,9)))
                
                Bot.locate('confirmar', wait=2)
                sleep(3)
            continue

        elif Bot.locate('codigouniversal', move=False, click=False, wait=0.25):
            if Bot.locate('codigo', wait=2):
                pg.typewrite('90311017', interval=0.08)
            Bot.locate('continuar', wait=2)
            sleep(2)
            continue

        elif Bot.locate('fichatecnica', move=False, click=False, wait=0.25):

            checklist = ['input', 'input2', 'input3', 'input4', 'input5', 'input6']

            for input in checklist:
                while True:
                    if Bot.locate(input, move=True, click=False):
                        Bot.locate('noaplica', move=True, click=True)
                        pg.scroll(-30)
                        Bot.locate('datosproducto', move=True, click=True)
                        continue
                    else: break
            for input in checklist:
                while True:
                    if Bot.locate(input, move=True, click=False):
                        Bot.locate('noaplica', move=True, click=True)
                        pg.scroll(-30)
                        Bot.locate('datosproducto', move=True, click=True)
                        continue
                    else: break
            sleep(0.2)
            pg.scroll(-800)
            Bot.locate('confirmar', check= True, wait=2)
            sleep(0.5)
            pg.scroll(-800)
            Bot.locate('siguiente', check= True, wait=2)
            sleep(2)
            continue

        # elif Bot.locate('ya_casi_publicas', move=False, click=False, wait=0.25):
        #     Bot.locate('cargar_direccion', wait=3)

        #     sleep(random.randint(3,5))

        #     Bot.locate('elegir', check=True, wait=2)
        #     pg.press('down', presses=1, interval=0.5)
        #     pg.press('enter')
        #     pg.press('tab')
        #     sleep(0.30)
        #     pg.typewrite(str(random.randint(21,87)), interval=random.randint(8,20)/100)
        #     pg.press('tab')
        #     sleep(0.30)
        #     pg.typewrite(str(random.randint(30,55)), interval=random.randint(8,20)/100)
        #     sleep(0.30)
        #     pg.press('tab')
        #     pg.typewrite(f"Piso {str(random.randint(1,20))} - Local {str(random.randint(1,150))}", interval=random.randint(8,20)/100)
        #     sleep(0.30)
        #     pg.press('tab')
        #     pg.typewrite(f"{str(random.randint(1,300))}", interval=random.randint(8,20)/100)
        #     sleep(0.10)
        #     pg.press('tab')
        #     pg.press('down', presses=random.randint(1,20), interval=random.randint(8,20)/100)
        #     sleep(2)
        #     pg.press('tab')
        #     pg.press('down', presses=random.randint(1,25), interval=random.randint(8,20)/100)
        #     sleep(0.30)
        #     pg.press('tab')
        #     sleep(0.30)
        #     distritos = ['Chachapoyas', 'Asuncion', 'Balsas', 'Cheto', 'Chiliquin', 'Chuquibamba', 'Cochabamba', 'Cochabamba', 'Granada', 'Huancas', 'La Jalca', 'Llata', 'Lucanas', 'Paijan', 'Pampas', 'Pomacocha', 'San Ignacio', 'San Juan', 'Santiago de Chuco', 'Tambobamba', 'Tingo', 'Tocmo', 'Tumbes', 'Yungay', 'Soloco', 'Sonche', 'La peca', 'Imaza', 'Florida', 'Recta', 'Conila', 'Luya']
        #     pg.typewrite(f"{str(random.choice(distritos))}", interval=random.randint(8,20)/100)
        #     Bot.locate('guardar_direccion', wait=3)
        #     Bot.locate('telefono', wait=5, check=True)
        #     pg.typewrite('950', interval=0.20)
        #     sleep(0.20)
        #     pg.typewrite(str(random.randint(235412,965487)), interval=0.25)
        #     Bot.locate('guardar_y_publicar', check=True, wait=10)
        
        elif Bot.locate('soles', move=False, click=False, wait=0.25):
            if Bot.locate('precio', move=False, click=False, wait=1) or Bot.locate('precio2'):
                read_txt(path, 'precio', copy=True, paste=True)
                Bot.locate('confirmar', wait=2)
                sleep(1)
            continue

        elif Bot.locate('tipopublicacion', move=False, click=False, wait=0.25):
            if Bot.locate('premium', wait=0.5):
                sleep(2)
                pg.scroll(-300)
                Bot.locate('confirmar_tipopublicacion', wait=2)
            sleep(1)
            continue
        
        elif Bot.locate('mercadoenvios', move=False, click=False, wait=0.25):
            Bot.locate('confirmar_mercadoenvios', wait=2)    
            sleep(1)
            continue

        elif Bot.locate('elige_un_domicilio', move=False, click=False, wait=0.25):
            domicilio = Bot.get_position('elige_un_domicilio', wait=2)
            pg.moveTo(domicilio[0]+35, domicilio[1]+130, duration=0.25)
            sleep(1)
            pg.click()
            sleep(2)
            continue

        elif Bot.locate('ofrecesretiro', move=False, click=False, wait=0.25):
            Bot.locate('retiro', wait=1)
            sleep(1)
            continue

        elif Bot.locate('mercadopago', move=False, click=False, wait=0.25):
            Bot.locate('continuar_mercadopago', wait=1)
            sleep(1)
            continue

        elif Bot.locate('ofrecesgarantia', move=False, click=False, wait=0.25) and not Bot.locate('garantia_check', move=False, click=False):
            Bot.locate('garantia')
            pg.typewrite('12', interval=0.05)           
            Bot.locate('confirmar_garantia', wait=2)   
            sleep(1)
            continue

        elif Bot.locate('descripcion', move=False, click=False, wait=0.25) and not Bot.locate('descripcion2', move=False, click=False):
            Bot.locate('descripcion', wait=1)

            if Bot.locate('descripcion2', wait=1):
                sleep(0.20)
                pg.typewrite(">>>> CARACTERISTICAS DEL PRODUCTO <<<<<", interval=0.05)
                sleep(0.2)
                pg.press('enter')
                sleep(0.2)
                pg.press('enter')
                sleep(0.3)
                read_txt(path, 'descripcion', copy=True, paste=True)
                sleep(0.20)
                pg.press('enter')
                sleep(0.20)
                pg.press('enter')
                sleep(0.20)
                pyperclip.copy(plantilla)
                pg.hotkey('ctrl', 'v')
                sleep(0.70)
                Bot.locate('descripcion')
                pg.scroll(-500)
                Bot.locate('confirmar_descripcion', wait=1)
                sleep(2)
            pg.scroll(-500)
            sleep(1)
                        
            Bot.locate('publicar', check=True, wait=2)
            sleep(5)
            pg.scroll(-10)
            Bot.locate('verpublicacion', check=True, wait=2)
            sleep(2)
            Bot.locate('soles_producto_publicado', move=False, click=False, check=True)
            pg.hotkey('ctrl', 'l')
            sleep(0.20)
            pg.hotkey('ctrl', 'c')
            sleep(0.20)
            link = pyperclip.paste()
            sleep(0.10)
            # desactivado por pruebas
            #telegram_report(f'{read_txt(path, "titulo")}\n{read_txt(path, "precio")} Soles\n{link}', '-1001781252897') # pg
            break

def post_email():

    if Bot.locate('profile'):

        profile_location = Bot.get_position('account_mail')
        pg.moveTo(profile_location[0]+80, profile_location[1]+30)
        sleep(0.20)
        pg.tripleClick(interval=0.02)
        pg.hotkey('ctrl', 'c')
        data = f"{pyperclip.paste()}"
        sleep(1)
        pg.click()
        
        telegram_report(f"{data}", '-734368278 ')