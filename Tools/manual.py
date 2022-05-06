import os, pyperclip, time, requests

telefono = '932 928 977'
serial = '90311017'
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

# ---------------- Finalizado  27/4/22 -----------------

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def leer_txt(ruta, nombre):
    try: 
        archivo = os.path.join(ruta, nombre+'.txt')
        with open(archivo, mode='r', encoding='utf-8') as txt:
            content = txt.read()
            print(content)
            return content

    except: print(f'Archivo invalido: {nombre}')

def revisar(ruta):
    limpiar_consola()
    print('[REVISANDO PRODUCTO]')
    print('\n- - - - Titulo - - - -')
    leer_txt(ruta, 'titulo')
    print('\n- - - - Descripcion - - - -')
    leer_txt(ruta, 'descripcion')
    print('\n- - - - Precio - - - -')
    leer_txt(ruta, 'precio')
    input('\n--- Presiona enter para salir ---\n')

def menu(ruta, titulo):

    contenido = f"""
- - - - - - - - - PRODUCTO - - - - - - - - - 

[{leer_txt(ruta, titulo)}]

- - - - - - - MENU DE OPCIONES - - - - - - -

[1] Ver y Copiar Titulo 
[2] Ver y Copiar Marca 
[3] Ver y Copiar Modelo
[4] Ver y Copiar Precio
[5] Ver y Copiar Descripcion 
[6] Ver y Copiar Plantilla
[7] Ver y Copiar Serial
[8] Ver y Copiar Telefono
[9] Ver y Copiar Ruta /img
[99] Revisar Producto

[0] Salir

- - - - - - - - - - - - - - - - - - - - - - - 
"""
    print(contenido)

def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)

def copiar_producto():

    telegram_report(f'Ejecutando manual.py desde {os.environ.get("USERNAME")}', '-757148301')
    limpiar_consola()
    ruta = input(r'[?] Ingrese ruta del producto: ')
    limpiar_consola()

    if os.path.isdir(ruta): 

        while True: 

            try: 
                menu(ruta, 'titulo')
                opcion = input('[?] Ingrese opcion: ')
                limpiar_consola()

                if int(opcion) == 1:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    pyperclip.copy(leer_txt(ruta, 'titulo'))
                    print('\n[+] Titulo copiado correctamente!')

                elif int(opcion) == 2:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    pyperclip.copy(leer_txt(ruta, 'marca'))
                    print('\n[+] Marca copiado correctamente!')
                    
                elif int(opcion) == 3:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    pyperclip.copy(leer_txt(ruta, 'modelo'))
                    print('\n[+] Modelo copiado correctamente!')

                elif int(opcion) == 4:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    pyperclip.copy(leer_txt(ruta, 'precio'))
                    print('\n[+] Precio copiado correctamente!')
                    
                elif int(opcion) == 5:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    pyperclip.copy(leer_txt(ruta, 'descripcion'))
                    print('\n[+] Descripcion copiado correctamente!')

                elif int(opcion) == 6:
                    pyperclip.copy(plantilla)
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    print(plantilla)
                    print('\n[+] Plantilla copiado correctamente!')

                elif int(opcion) == 7:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    print(serial)
                    pyperclip.copy(serial)
                    print('\n[+] Serial copiado correctamente!')

                elif int(opcion) == 8:
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    print(telefono)
                    pyperclip.copy(telefono)
                    print('\n[+] Telefono copiado correctamente!')

                elif int(opcion) == 9:
                    img = os.path.join(ruta, 'img')
                    print('\n - - - - - - CONTENIDO - - - - - -\n')
                    print(str(img))
                    pyperclip.copy(img)
                    print('\n[+] Ruta /img copiado correctamente!')

                elif int(opcion) == 99:
                    revisar(ruta)

                elif int(opcion) == 0: 
                    print('[-] Saliendo...')
                    time.sleep(0.5)
                    limpiar_consola()
                    break
                
                else: print('[-] Opcion Invalida')

                time.sleep(0.5)
                limpiar_consola()

            except: 
                limpiar_consola()
                print('[-] Opcion invalida')
                time.sleep(1)

if __name__ == '__main__':
    while True: 
        copiar_producto()
        