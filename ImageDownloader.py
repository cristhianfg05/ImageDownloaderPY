import urllib.request

def dwlImg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Url de la imagen: ')
file_name = input('Nombre de la imagen a guardar: ')

dwlImg(url, 'images/', file_name)