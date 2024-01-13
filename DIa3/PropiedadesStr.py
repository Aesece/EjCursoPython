nombre = "Carina"
#nombre[0]="K"  #No se puede ejecutar ya que no pueden cambiarse un objeto String
print(nombre)

n1 = "Kari"
n2 = "na"
print(n1+n2) # Strings se pueden concatenar
print(n1*5) #Tambien pueden multiplicarse

poema=  """Mil pequeños peces blancos
como si hirviera
el color del agua"""   ##Puede haber saltos de linea poniendo tres comillas dobles
print(poema)

print("agua" in poema)  #Verifica si existe el parametro en una cadena dada
print("agua" not in poema)  #Tambien funciona con negaciones

print(len(poema)) #len verifica la longitud de la cadena