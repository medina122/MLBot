import os
from time import sleep
from funciones import crear_txt, read_txt, telegram_report


def listar_productos(path):
    
    # Listamos y obtenemos los productos
    mainfolder = os.listdir(path)

    for folder in mainfolder:
        
        if folder.endswith('.txt'):
            break
        else:
            # Leemos cada carpeta y obtenemos el contenido
        
            producto = str(path) + '/' + str(folder)
            info = f"""{read_txt(producto, 'titulo')} - {read_txt(producto, 'precio')}"""

            # Agregamos la informacion a un documento txt 
            crear_txt(path, 'productos', info)
            sleep(0.10)


def report_list(path):
    
    listar_productos(path)

    sleep(0.5)
    txt = read_txt(path, 'productos')

    sleep(0.5)
    telegram_report(f"""Productos:\n\n{txt}""", '2112636737')


   
    