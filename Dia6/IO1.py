mi_archivo = open('prueba.txt')
print(mi_archivo)
print(mi_archivo.read()) ##Retorna todoo el archivo
mi_archivo.close()  ##Se tiene que cerrar el archivo

mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()  ##Lee las lineas y guarda donde se quedo
print(una_linea.upper())
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
una_linea = mi_archivo.readline()
print(una_linea)



mi_archivo = open('prueba.txt')
for l in mi_archivo: ## Se puede iterar como strings de cada linea
    print("Linea: "+l)
mi_archivo.close()

mi_archivo = open('prueba.txt')
todas = mi_archivo.readlines() ##Se lo trata como lista
print(todas)
