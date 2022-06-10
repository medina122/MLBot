from time import sleep
import os

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Funcion para leer archivos txt a traves de rutas y nombres
def leer_txt(ruta, nombre):
    archivo = os.path.join(ruta, nombre) + '.txt'
    with open(archivo, 'r', encoding='utf8') as file:
        return file.read()

# Funcion para crear archivos txt mediante nombre y contenido
def crear_txt(nombre, metodo, contenido):
    with open(nombre+'.txt', metodo, encoding="utf8") as file:
        file.write(contenido)
        file.close()

# Funcion para listar una carpeta de productos
def listar_carpeta(carpeta, reporte):
    
    for producto in os.listdir(carpeta):
        ruta = os.path.join(carpeta, producto)
        informacion = f"{leer_txt(ruta, 'titulo')} - {leer_txt(ruta, 'precio')}"

        print(informacion)
        if reporte == 'y': crear_txt('reporte', 'a', informacion+'\n')
        

# Funcion para listar productos de subcarpetas de una carpeta
def listar_carpetas(carpeta, reporte):
    # Obtenemos los nombres de los subdirectorios
    for categoria in os.listdir(carpeta):
        subcarpeta = os.path.join(carpeta, categoria)
        # Recorremos cada producto de los subdirectorios
        for producto in os.listdir(subcarpeta):
            try:
                ruta = os.path.join(carpeta, subcarpeta, producto)
                informacion = f"{leer_txt(ruta, 'titulo')} - {leer_txt(ruta, 'precio')}"

                print(informacion)
                if reporte == 'y': crear_txt('reporte', 'a', informacion+'\n')
            except: print('Algo salio mal')

menu = """
-------------------------------------

LISTAR PRODUCTOS:

Opciones: 

1 - Listar carpeta
2 - Listar grupo de carpetas

--------------------------------------
"""

def listar_productos():
    try:
        limpiar_consola()
        print(menu)
        opcion = input('Ingrese opcion: ')
        limpiar_consola()

        if int(opcion) == 1:
            ruta = input(r"Ingrese ruta de la carpeta a listar: ")
            reporte = input('¿Desea generar reporte? (y/n): ')
            # limpiar_consola()
            listar_carpeta(ruta, reporte)
            sleep(2)

        elif int(opcion) == 2: 
            ruta = input(r"Ingrese ruta de las carpetas a listar: ")
            reporte = input('¿Desea generar reporte? (y/n): ')
            limpiar_consola()
            listar_carpetas(ruta, reporte)

    except: print('Opcion invalida')

if __name__ == "__main__":
    
    while True:
        listar_productos()
