import os
from time import sleep

def leer_archivo_del_producto(ruta, nombre_del_archivo):
    archivo = os.path.join(ruta, nombre_del_archivo) + '.txt'
    
    with open(archivo, 'r', encoding='utf8') as file: 
        data = file.read()
        return data

def crear_reporte(contenido):
    
    with open('reporte.txt', 'a', encoding='utf8') as file:
        file.write(contenido)
        file.close()

def listar_productos(): # Global

    carpeta_principal = r"C:\Users\owner\Desktop\Projects\MLBot\AmazonDB" # AmazonDB

    lista_de_carpetas = os.listdir(carpeta_principal)

    for categoria in lista_de_carpetas:
        
        subcarpetas = os.path.join(carpeta_principal, categoria)
        
        for subcarpeta in os.listdir(subcarpetas):
        
            ruta_de_la_subcarpeta = os.path.join(subcarpetas, subcarpeta)
            informacion_requerida = f"{leer_archivo_del_producto(ruta_de_la_subcarpeta, 'titulo')} -- {leer_archivo_del_producto(ruta_de_la_subcarpeta, 'precio')}\n"
            crear_reporte(informacion_requerida)
            sleep(0.05)

def listar_productos_una_carpeta():

    carpeta = r'C:\Users\owner\Desktop\Projects\MLBot\AmazonDB\1-GPU'

    for producto in os.listdir(carpeta):
        ruta_de_la_subcarpeta = os.path.join(carpeta, producto)
        informacion_requerida = f"{leer_archivo_del_producto(ruta_de_la_subcarpeta, 'titulo')} -- {leer_archivo_del_producto(ruta_de_la_subcarpeta, 'precio')}\n"
        crear_reporte(informacion_requerida)
        sleep(0.05)

listar_productos_una_carpeta()