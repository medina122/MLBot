import os
from time import sleep
from funciones import listar_productos, clear, telegram_report
from post import post, post_email
from generate_id import generar

# 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

menu = """
Menu de Opciones: 

1- Publicar producto 
2- Publicar grupo de productos
3- Enlistar productos
4- Generar ID
"""

if __name__ == '__main__':
    while True: 
        clear()
        print(menu)
        opcion = input('>> ')

        if int(opcion) == 1:

            path = input(r'Ingrese carpeta del producto: ')
            post(path)
            post_email()

        elif int(opcion) == 2:
            
            telegram_report(f'Publicando desde: {os.environ.get("USERNAME")}', '-1001781252897') # BOT
            
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
            
            