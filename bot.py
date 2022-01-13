import pyautogui as bot, os, pyperclip, random
from time import sleep
from funciones import listar_productos
from post import post, post_email
from generate_id import generar

menu = """

Menu de Opciones: 

1- Publicar producto y reportar por telegram
2- Publicar grupo de productos y reportar por telegram
3- Enlistar productos
4- Generar ID

"""

if __name__ == '__main__':
    while True: 

        print(menu)
        opcion = input('>> ')

        if int(opcion) == 1:

            path = input(r'Ingrese carpeta del producto: ')
            post(path)
            post_email()

        elif int(opcion) == 2:
            
            mainfolder = input(r'Ingrese carpeta de los productos: ')
            
            for folder in os.listdir(mainfolder):

                path = ''

                if mainfolder.startswith('C:'):

                    path = mainfolder + f'\{folder}'  

                else: 
                    
                    path = mainfolder + f'/{folder}'  

                post(path)
            
            sleep(2)

            post_email()

            listar_productos(mainfolder)

        elif int(opcion) == 3:
            path = input('Ingrese ruta de de productos a listar: ')
            listar_productos(path, report=False)

        elif int(opcion) == 4:
            generar()
            
            