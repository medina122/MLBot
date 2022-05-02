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

def nuevo_producto():
    limpiar_consola()
    ruta = input(r'Ingrese ruta del producto: ')

    if os.path.isdir(ruta):
        
        while True:
            limpiar_consola()
            print(opciones)
            opcion = input('Ingrese opcion: ')
            limpiar_consola()

            if int(opcion) == 1: 
                crear_txt(ruta,'titulo', input('Ingrese titulo: '))
            elif int(opcion) == 2: 
                crear_txt(ruta,'marca', input('Ingrese marca: '))
            elif int(opcion) == 3: 
                crear_txt(ruta,'modelo', input('Ingrese modelo: '))
            elif int(opcion) == 4: 
                crear_txt(ruta,'precio', input('Ingrese precio: '))
            elif int(opcion) == 5: 
                sin_procesar = []
                while True: 
                    linea = input('Ingrese contenido: ')
                    if linea:
                        sin_procesar.append(linea)
                    else: break
                contenido = '\n'.join(sin_procesar)
                crear_txt(ruta,'descripcion', contenido)
            elif int(opcion) == 6: 
                crear_txt(ruta, 'url', input('Ingrese url: '))
            elif int(opcion) == 9: break

if __name__ == '__main__':
    while True:
        nuevo_producto()