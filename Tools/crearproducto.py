import os, requests

opciones = """

Opciones:

1 - Agregar titulo
2 - Agregar marca
3 - Agregar modelo
4 - Agregar precio
5 - Agregar descripcion
6 - Agregar url
7 - Agregar imagenes
8 - Agregar fotos reales
9 - Crear otro producto

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

def descargar_imagen(titulo, url):
    respuesta = requests.get(url)
    archivo = open(titulo+'.jpg', 'wb')
    archivo.write(respuesta.content)
    archivo.close()

def nuevo_producto():
    
    limpiar_consola()
    carpeta_principal = input(r'Ingrese la ruta de la carpeta principal donde se crearan los productos: ')
    
    while True:

        if os.path.isdir(carpeta_principal):
            
            limpiar_consola()
            producto = input('Ingrese titulo de la carpeta del producto: ')

            if producto != '':

                nuevo_producto = os.path.join(carpeta_principal, producto)
                os.mkdir(nuevo_producto)

                while True:
                    limpiar_consola()
                    print(f'Carpeta actual: {producto}')
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

                            print("Pega la descripcion del producto. \n\nPD: El archivo se cierra automaticamente si hay un espacio en blanco\n")

                            while True: 
                                linea = input('>>>')
                                if linea:
                                    sin_procesar.append(linea)
                                else: break
                            contenido = '\n'.join(sin_procesar)
                            crear_txt(nuevo_producto,'descripcion', contenido)
                        elif int(opcion) == 6: 
                            crear_txt(nuevo_producto, 'url', input('Ingrese url: '))
                            
                        elif int(opcion) == 7:
                            os.mkdir(os.path.join(nuevo_producto, 'img'))

                            contador = 1
                            imagenes = []

                            imagen = input('Ingrese URL de la imagen a descargar: ')
                            imagenes.append(imagen)

                            while True:
                                imagen = input('Ingrese URL de la siguiente imagen o deje en blanco para terminar: ')

                                if imagen != '': 
                                    imagenes.append(imagen)
                                elif imagen == '':
                                    break
                                else: print('Ingrese una opcion valida')
                        
                            print('Descargando archivos... Por favor espere')

                            for imagen in imagenes:
                                ruta = os.path.join(nuevo_producto, 'img', str(contador))
                                descargar_imagen(ruta, url=imagen)
                                contador +=1

                            print('Descarga exitosa!')

                        elif int(opcion) == 8:

                            os.mkdir(os.path.join(nuevo_producto, 'fotos'))

                            contador = 1
                            imagenes = []

                            imagen = input('Ingrese URL de la imagen a descargar: ')
                            imagenes.append(imagen)

                            while True:
                                imagen = input('Ingrese URL de la siguiente imagen o deje en blanco para terminar: ')

                                if imagen != '': 
                                    imagenes.append(imagen)
                                elif imagen == '':
                                    break
                                else: print('Ingrese una opcion valida')
                            
                            print('Descargando archivos... Por favor espere')

                            for imagen in imagenes:
                                ruta = os.path.join(nuevo_producto, 'fotos', str(contador))
                                descargar_imagen(ruta, url=imagen)
                                contador +=1
                            
                            print('Descarga exitosa!')

                        elif int(opcion) == 9: break
                    except: continue
        else: break

if __name__ == '__main__':
    nuevo_producto()