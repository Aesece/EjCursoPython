##Modos de apertura r= solo lectura, w=solo escritura, a=solo escritura al final del archivo
file = open('prueba.txt','r')  ##SOlo lectura
file.write("textoPrueba")
file.close()

file = open('prueba2.txt','w')  ###Escritura, reemplaza el texto contenido, si no existe el archivo lo crea
file.write("textoPrueba\n")       ##No genera salto de linea a menos que se especifique con \n o con tres comillas
file.close()

file = open('prueba.txt','w')  #
file.writelines(['hola', 'mundo','aqio','estoy'])   ##Se puede escribir una lista de string
file.close()

file = open('prueba.txt','a')  ###Abre el archivo en modo escritura respetando lo que ya hay posicionandose al final
file.write("textoPrueba")
file.close()

