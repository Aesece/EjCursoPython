#Iguales a las listas pero no se pueden cambiar ni editar valores

mi_tuple=(1,2,3,4,5,1)
print(type(mi_tuple))

t= (5,2.3, 'ad')
print(t[-1])

t2=(1,2,3,4,(1,2,3),5,6) # Puede haber tuplas dentro de tuplas
print(t2[4][1])

mi_tuple = list(mi_tuple) #Se puede castear el tipo

x,y,z=t
print(x,y,z)

print(len(mi_tuple))

print(mi_tuple.count(1))