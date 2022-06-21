import os

info = """

--------------------------------------------------------------------

   VERIFICA CUANTOS CARACTERES CONTIENE EL TITULO DEL PRODUCTO

 Pega el titulo para imprimir en pantalla la cantidad de caracteres
                            que contiene

--------------------------------------------------------------------
"""

def main():
    print(info)
    texto = input('>>> ')
    caracteres = len(texto)

    if caracteres >= 60:

        print(f"\nEl titulo contiene {caracteres} caracteres y NO es admisible")

    elif caracteres <= 60:
        print(f"\nEl titulo contiene {caracteres} caracteres y es admisible")

    else: print('\nAlgo ha salido mal!')

    input('\nPresione cualquier tecla para finalizar...')

def limpiar_consola():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

while True:
    limpiar_consola()
    main()