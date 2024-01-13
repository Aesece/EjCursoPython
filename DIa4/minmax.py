#Regresa el valor minimo o maximo de la lista ingresada
menor = min(50,65,31,48,95,10,35)
mayor = max(50,65,31,48,95,10,35)
print(menor)
print(mayor)

lista = [50,65,31,48,95,10,35]
print(f"El menor es{min(lista)} y el mayor {max(lista)}")

nombres = ['Juan','Ana','Alicia','Predro']
print(min(nombres))

nombre= 'Carlos'   ##Puede funcionar con Strings ordenando alfabeticamente
print(min(nombre))  ###EMpieza buscando por mayusculas y luego minusculas

dic={'c1':42,'c2':11} ##Toma la key por defecto a menos que se indique con .values()
print(min(dic))