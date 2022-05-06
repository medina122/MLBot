import os

opciones = """

Opciones:

1 - Agregar titulo
2 - Agregar marca
3 - Agregar modelo
4 - Agregar precio
5 - Agregar descripcion
6 - Agregar url
9 - Salir

"""
def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def crear_txt(ruta, titulo, contenido):
    archivo = os.path.join(ruta, titulo+'.txt')
    with open(archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
        archivo.close()

# Parece que esta terminado 02/05/22 8:34PM
def nuevo_producto():
    
    limpiar_consola()
    carpeta_principal = input(r'Ingrese la ruta donde se crearan los productos: ')
    
    while True:

        if os.path.isdir(carpeta_principal):
            
            limpiar_consola()
            producto = input('Ingrese titulo de la carpeta del producto: ')

            if producto != '':

                nuevo_producto = os.path.join(carpeta_principal, producto)
                os.mkdir(nuevo_producto)
                os.mkdir(os.path.join(nuevo_producto, 'img'))
                os.mkdir(os.path.join(nuevo_producto, 'fotos'))

                while True:
                    limpiar_consola()
                    print(opciones)
                    opcion = input('Ingrese opcion: ')
                    try:
                        limpiar_consola()
                        if int(opcion) == 1: 
                            crear_txt(nuevo_producto,'titulo', input('Ingrese titulo: '))
                        elif int(opcion) == 2: 
                            crear_txt(nuevo_producto,'marca', input('Ingrese marca: '))
                        elif int(opcion) == 3: 
                            crear_txt(nuevo_producto,'modelo', input('Ingrese modelo: '))
                        elif int(opcion) == 4: 
                            crear_txt(nuevo_producto,'precio', input('Ingrese precio: '))
                        elif int(opcion) == 5: 
                            sin_procesar = []
                            while True: 
                                linea = input('Ingrese contenido: ')
                                if linea:
                                    sin_procesar.append(linea)
                                else: break
                            contenido = '\n'.join(sin_procesar)
                            crear_txt(nuevo_producto,'descripcion', contenido)
                        elif int(opcion) == 6: 
                            crear_txt(nuevo_producto, 'url', input('Ingrese url: '))
                        elif int(opcion) == 9: break
                    except: continue
        else: break

if __name__ == '__main__':
    nuevo_producto()