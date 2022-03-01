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

def listar_productos():

    carpeta_principal = r"C:\Users\owner\Desktop\Projects\MLBot\AmazonDB" # AmazonDB

    lista_de_carpetas = os.listdir(carpeta_principal)

    for categoria in lista_de_carpetas:
        
        subcarpetas = os.path.join(carpeta_principal, categoria)
        
        for subcarpeta in os.listdir(subcarpetas):
        
            ruta_de_la_subcarpeta = os.path.join(subcarpetas, subcarpeta)
            informacion_requerida = f"{leer_archivo_del_producto(ruta_de_la_subcarpeta, 'titulo')} -- {leer_archivo_del_producto(ruta_de_la_subcarpeta, 'precio')}\n"
            crear_reporte(informacion_requerida)
            sleep(0.05)
