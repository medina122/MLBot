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

def main():
    cuenta = input('Ingrese correo electronico: ')
    carpeta = input(r'Ingrese ruta a listar: ')

    listar_carpetas(carpeta)
    telegram_report(f"Publicando desde: {cuenta}\n\n{leer_txt(carpeta, 'reporte')}", '-734368278')
    reporte = os.path.join(carpeta, 'reporte.txt')
    os.remove(reporte)

if __name__ == '__main__':
    while True:
        main()