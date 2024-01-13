#Se pueden hacer los mismos metodos que con los Strings
mlist = ['a','b','c']
mlist2 = ['d','e','f']
olist = ['Hola',5,2.4,'b'] #Pueden contener elementos de diferente tipo
print(type(mlist))
print(len(olist))
res = mlist[0:3]
print(res)

print(mlist2+mlist2)
mlist3 = mlist+mlist2
# Sus elementos pueden ser cambiados

mlist3[0] = 'alpha'
print(mlist3)
mlist3.append('g') #Se usa append para agregar elementos a la lista
print(mlist3)
elim=mlist3.pop(0) #Elimina un elemento;parametro es el indice a eliminar, sin parametros elimina el ultimo elemento de la lista.
#Tambien se puede guardar el valor popeado en una variable
print(mlist3)
print(elim)
mlist4 = ['f','z','q','a','c','b']
mlist4.sort() #Ordena la lista sobre la que se aplica la funcion sin asignar
print(mlist4)

mlist4.reverse()
print(mlist4) #al igual que sort no devuelve la lista solo la reordena en reversa

redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]
redes.sort()
print(redes)
