import requests, os, time, colorama
from lxml import html
from colorama import Fore

# Inicializamos Colorama para darle color a los textos
colorama.init()

# Creamos las funciones que vamos a utilizar

def limpiar_consola(): # Para limpiar la consola cada vez que lo necesitemos
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def normalizar(cadena:str): # Elimina acentos de las cadenas y reemplaza espacios en blanco para los titulos

    letras = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u'
    }

    for letra in ['á', 'é','í', 'ó', 'ú']:

        if cadena.find(letra): cadena = cadena.replace(letra, letras[letra])

    if cadena.find(' '): cadena = cadena.replace(' ', '_')

    return cadena.lower()

def leer_txt(titulo:str): # Lee archivos txt
    with open(titulo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def crear_txt(ruta:str, titulo:str, contenido:str): # Crea archivos txt


    archivo_final = os.path.join(ruta, normalizar(titulo)) + '.txt'
    with open(archivo_final, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
        archivo.close()

def descargar_imagenes(carpeta:str, lista:list): # Descarga imagenes a traves de una lista de URLs
    
    # Asignamos el titulo de cada imagen segun un numero que ira en aumento segun la cantidad de imagenes
    titulo = 1

    # Listamos cada imagen para poder procesarla correctamente
    for imagen in lista:
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Descargando imagen: {imagen}")
        # Descargamos la imagen
        respuesta = requests.get(imagen)
        # Asignamos el titulo con la ubicacion correspondiente
        ruta_final = os.path.join(carpeta, str(titulo)) + '.jpg'
        # La guardamos en un archivo nuevo
        with open(ruta_final, 'wb') as imagen:
            imagen.write(respuesta.content)
            imagen.close()
        titulo += 1

def descargar_productos(carpeta, url):

    print("[+] Iniciando descarga...")

    # Descargamos el HTML de la pagina
    pagina = requests.get(url)
    tree = html.fromstring(pagina.content)

    print(f"{Fore.GREEN}[+]{Fore.WHITE} Obteniendo datos...")
    time.sleep(0.2)

    # Ubicamos los elementos a traves de XPATH en el HTML
    titulo = tree.xpath('/html/body/main/div/div[4]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/h1/text()')[-0]
    precio = tree.xpath('//div[@class="ui-pdp-price__second-line"]/span/span[3]/text()')[0]
    caracteristicas_titulo = tree.xpath('//th/text()')
    caracteristicas_informacion = tree.xpath('//td/span/text()')

    print(f"{Fore.GREEN}[+]{Fore.WHITE} Extrayendo informacion del {titulo}")
    time.sleep(0.1)

    # Procesamos el titulo para crear la carpeta correctamente

    print(f"{Fore.GREEN}[+]{Fore.WHITE} Procesando el titulo...")
    time.sleep(0.1)

    titulo_carpeta = titulo

    if str(titulo_carpeta).find('/'): titulo_carpeta = str(titulo_carpeta).replace('/', '')

    if str(titulo_carpeta).find('|'): titulo_carpeta = str(titulo_carpeta).replace('|', '')

    if str(titulo_carpeta).find('*'): titulo_carpeta = str(titulo_carpeta).replace('*', '')
    
    if str(titulo_carpeta).find("'"): titulo_carpeta = str(titulo_carpeta).replace("'", '')

    if str(titulo_carpeta).find('     '): titulo_carpeta = str(titulo_carpeta).replace("     ", ' ')
    
    if str(titulo_carpeta).find('    '): titulo_carpeta = str(titulo_carpeta).replace("    ", ' ')
    
    if str(titulo_carpeta).find('   '): titulo_carpeta = str(titulo_carpeta).replace("   ", ' ')

    if str(titulo_carpeta).find('  '): titulo_carpeta = str(titulo_carpeta).replace("  ", ' ')
    
    if str(titulo_carpeta).endswith(' '): titulo_carpeta = titulo_carpeta[:-1]

    # Verificamos que la carpeta del producto exista, de lo contrario la creamos
    producto = os.path.join(carpeta, titulo_carpeta)

    if os.path.isdir(producto):
        print(f"{Fore.GREEN}[+]{Fore.WHITE} La carpeta del producto existe, utilizando la actual...")

    else: 
        os.mkdir(producto)
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Creando la carpeta del producto...")
        time.sleep(0.2)

    # Creamos el titulo del producto
    crear_txt(producto, 'titulo', titulo)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando Titulo...")
    time.sleep(0.1)

    # Creamos el titulo del producto
    crear_txt(producto, 'url', url)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando Url...")
    time.sleep(0.1)

    caracteristicas = len(caracteristicas_titulo)

    if caracteristicas > 1:
        crear_txt(producto, caracteristicas_titulo[0], caracteristicas_informacion[0])
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando {caracteristicas_titulo[0]}")
        time.sleep(0.1)

    if caracteristicas > 2:
        crear_txt(producto, caracteristicas_titulo[1], caracteristicas_informacion[1])
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando {caracteristicas_titulo[1]}")
        time.sleep(0.1)

    if caracteristicas > 3:
        crear_txt(producto, caracteristicas_titulo[2], caracteristicas_informacion[2])
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando {caracteristicas_titulo[2]}")
        time.sleep(0.1)

    if caracteristicas > 4:
        crear_txt(producto, caracteristicas_titulo[3], caracteristicas_informacion[3])
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando {caracteristicas_titulo[3]}")
        time.sleep(0.1)

    # Extraemos la descripcion
    descripcion_lista = tree.xpath('//p[@class="ui-pdp-description__content"]/text()')
    descripcion = '\n'.join(descripcion_lista)
    crear_txt(producto, 'descripcion', descripcion)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} Guardando Descripcion")
    time.sleep(0.1)

    # Extraemos las imagenes para recorrerlas y descargarlas
    imgs = tree.xpath('//img/@data-zoom')

    # Verificamos si la carpeta img del producto existe, de lo contrario la creamos

    if os.path.isdir(os.path.join(producto, 'img')): pass
    
    else: 
        os.mkdir(os.path.join(producto, 'img'))
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Creando carpeta /img")
        time.sleep(0.1)

    descargar_imagenes(os.path.join(producto, 'img'), imgs)
    print(f"{Fore.GREEN}[+]{Fore.WHITE} Producto descargado y almacenado correctamente en la Base de Datos!")
    time.sleep(0.1)

    print('\n---------------------------------------------\n')
    print(f'Titulo: {titulo}')
    print(f'Precio: S/ {precio}')
    print('---------------------------------------------')

if __name__ == '__main__':

    carpeta = r'C:\Users\owner\Desktop\Projects\MLBot\Nuevos'
    
    while True:

        productos = []

        while True:
            insertar_nuevo_producto = input('Ingrese el enlace o deje en blanco para continuar: ')
            
            if insertar_nuevo_producto != '':
                productos.append(str(insertar_nuevo_producto))
            elif insertar_nuevo_producto == '':
                break

        print(f"[?] Descargando lista de productos...")

        contador = 0
        for producto in productos:
            descargar_productos(carpeta, producto)
            contador += 1
            time.sleep(1)
            print(f"{Fore.GREEN}[+]{Fore.WHITE}Descargas exitosas: {str(contador)}")
            print('\n')