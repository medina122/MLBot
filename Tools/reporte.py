import os, requests, colorama
from colorama import Fore

colorama.init()

def leer_txt(ruta, nombre):
    archivo = os.path.join(ruta, nombre) + '.txt'
    with open(archivo, 'r', encoding='utf8') as file:
        return file.read()

def crear_txt(ruta, nombre, metodo, contenido):
    archivo = os.path.join(ruta, nombre+'.txt')
    with open(archivo, metodo, encoding="utf8") as file:
        file.write(contenido)
        file.close()

def telegram_report(txt, chatid):
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")

def listar_carpetas(carpeta):
    for producto in os.listdir(carpeta):
        subcarpeta = os.path.join(carpeta, producto)
    
        informacion = f"{leer_txt(subcarpeta, 'titulo')} - {leer_txt(subcarpeta, 'precio')}"
        crear_txt(carpeta, 'reporte', 'a', informacion+'\n')

def generar_reporte():
    try: 
            carpeta = input(r'Ingrese ruta a listar: ')
            cuenta = input('Ingrese correo electronico: ')

            listar_carpetas(carpeta)
            telegram_report(f"Cuenta:  {cuenta}\n\nProductos: \n\n{leer_txt(carpeta, 'reporte')}", '-1001758383002')
            os.remove(os.path.join(carpeta, 'reporte.txt'))
    except:
        print('Datos no validos')
        exit()
    
info = """

---------------------------------------------------------

- - REPORTAR CUENTA PUBLICADA EN EL CANAL DE TELEGRAM - -

Requiere del correo electronico donde los productos fueron
publicados para posteriormente listarlos y subirlos a un
canal de telegram para poder llevar mejor control de todo

---------------------------------------------------------
"""
if __name__ == '__main__':
    while True:
        generar_reporte()