import os

def corregir_archivo(path, name, content): 
    
    data = ''

    if path.startswith('C:'):

        data = path + f'\{name}.txt'  

    else: 
        data = path + f'/{name}.txt'  

    with open(data, 'w') as file:
        file.write(content)
        file.close()


mainfolder = r'C:\Users\Owner\Desktop\MLBot\AmazonDB\Ofertas'
for product in os.listdir(mainfolder):
    content = '950235631'

    if mainfolder.startswith('C:'):

        data = mainfolder + f'\{product}'  

    else: 
        data = mainfolder + f'/{product}'  

    corregir_archivo(data, 'telefono', content)