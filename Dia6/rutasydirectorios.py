import os
from pathlibbb import Path

ruta = os.getcwd() ##Obtiene el directorio de trabajo actual
print(ruta)

ruta = os.chdir('C:\\Users\\QA\\Documents\\QA_SCV\\PRBMOI\\documentacion') ##Cambia de directorio de trabajo
ruta = os.makedirs('C:\\Users\\QA\\Documents\\QA_SCV\\PRBMOI\\documentacion\\otra') ##crea y cambia a una nueva direccion

ruta = 'C:\\Users\\QA\\Documents\\Curso Python\\Projects\\PrimerProyecto\\Dia6\\prueba.txt'
elemento = os.path.basename(ruta)   ##Obtiene la parte del nombre de archivo
elemento = os.path.dirname(ruta) ##Obtiene el directorio de ruta
elemento = os.path.split((ruta))  ##regresa una tupla con el directorio y el nombre de archivo

os.rmdir('C:\\Users\\QA\\Documents\\QA_SCV\\PRBMOI\\documentacion\\otra')  ##Elimina un directorio del sistema

archivo = open('C:\\Users\\QA\\Documents\\QA_SCV\\PRBMOI\\documentacion\\pruebasrutas.txt') ## con la ruta completa se abre un archivo



carpeta = Path('/Users/QA/Documents/QA_SCV/PRBMOI/documentacion')
archivo = carpeta /'pruebasrutas.txt'  #crea un objeto tipo path para crear un archivo
mi_archivo = open(archivo)
print(mi_archivo.read())


