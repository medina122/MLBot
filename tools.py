from Tools.manual import copiar_producto
from Tools.reporte import generar_reporte
from Tools.listarproductos import listar_productos 
from Tools.generarid import generar_identidad
from Tools.crearproducto import nuevo_producto
import time, os
menu = """
- - - - - - HERRAMIENTAS - - - - - - 

1 - Publicar producto manualmente
2 - Realizar reporte
3 - Listar productos 
4 - Generar ID 
5 - Crear producto nuevo

- - - - - - - - - - - - - - - - - - -
"""

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

while True:
    try: 
        limpiar_consola()
        print(menu)
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1: copiar_producto()
        elif opcion == 2: generar_reporte()
        elif opcion == 3: listar_productos()
        elif opcion == 4: generar_identidad()
        elif opcion == 5: nuevo_producto()
        
    except:
        limpiar_consola()
        print('Opcion invalida')
        time.sleep(0.35)
        limpiar_consola()
