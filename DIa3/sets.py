#Sets son iguales que las listas pero no estan indexados y sus elementos no pueden repetirse

mi_set = set([1,2,3,4,5,6])
print(type(mi_set))
print(mi_set)

oset = {1,2,3,4,5}
print(type(oset))
print(oset)

print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3,4,5,5}
s2 = {3,4,6,7}
s3 = s1.union(s2)  #Une dos sets, conjuntos o colecciones

print(s3)

s1.add(9) #agrega elemento indicado al conjunto, si ya existe lo descarta
print(s1)

s1.remove(4) #Elimina un elemento que debe de existir en el set
s1.discard(2) #Elimina un elemento que puede o no existir en el set, si no existe, lo descarta
print(s1)

s=s1.pop() #Elimina un elemento aleatorio en el set
print(s)

s1.clear()  #Vacia el set
print(s1)


