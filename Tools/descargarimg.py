import requests, os

info = """

--------------------------------------------------------------

- - - - HECHO PARA DESCARGAR IMAGENES A TRAVES DE URLS - - - - 

Requiere pasarle distintos links para agregarlos a una lista
para posteriormente ser descargados y almacenados en la ruta 
que especifiques

--------------------------------------------------------------
"""

def descargar_imagen(titulo, url):
    respuesta = requests.get(url)
    archivo = open(titulo+'.jpg', 'wb')
    archivo.write(respuesta.content)
    archivo.close()

contador = 1
imagenes = []

print(info)

carpeta = input(r'Ingrese ruta donde desea guardar las imagenes: ')

if os.path.isdir(carpeta):

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
        ruta = os.path.join(carpeta, str(contador))
        descargar_imagen(ruta, url=imagen)
        contador +=1

    print('Descarga exitosa!')
    