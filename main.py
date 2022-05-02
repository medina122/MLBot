import os
from time import sleep
from Tools.funciones import listar_productos, limpiar_consola, telegram_report
from Tools.post import post, post_email
from Tools import generarid

# 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

menu = """
Menu de Opciones: 

1- Publicar producto 
2- Publicar grupo de productos
3- Enlistar productos
4- Generar ID
5- Modificar precios

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
            
            
            mainfolder = input(r'Ingrese carpeta de los productos: ')
            # Desactivado porque estoy haciendo testeos
            #telegram_report(f'Publicando desde: {os.environ.get("USERNAME")}', '-1001781252897') # BOT
            #post_email()
                    
            for folder in os.listdir(mainfolder):

                path = os.path.join(mainfolder, folder)
                post(path)
            
            sleep(2)
            listar_productos(mainfolder)
            # Desactivado porque estoy haciendo testeos
            #telegram_report(f'Publicado desde: {os.environ.get("USERNAME")}', '-734368278') # BOT


        elif int(opcion) == 3:
            path = input('Ingrese ruta de de productos a listar: ')
            listar_productos(path)


        elif int(opcion) == 4:
            generarid()
            
            