import os

# Funcion para limpiar consola en Windows o Linux
def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)