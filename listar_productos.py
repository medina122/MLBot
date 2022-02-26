import os

def listar_productos():

    carpeta_principal = r"C:\Users\owner\Desktop\Projects\MLBot\AmazonDB" # AmazonDB

    lista_de_carpetas = os.listdir(carpeta_principal)

    for categoria in lista_de_carpetas:
        
        subcarpetas = os.path.join(carpeta_principal, categoria)
        
        for producto in os.listdir(subcarpetas):
        
            path = os.path.join(subcarpetas, producto)
            print(path)


listar_productos()