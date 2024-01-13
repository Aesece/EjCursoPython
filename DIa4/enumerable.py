lista = ['a', 'b','c']

for i, item in enumerate(lista): #Se enumera y muestra una serie de tuplas conformadas por indice y valor
     print(i,item)

for i,item in enumerate(range(50,55)): ##Se puede usar dentro de un loop
    print(i,item)

mi_tuplas =list(enumerate(lista)) ##Se puede castear una lista directamente de enumerar otro objeto
print(mi_tuplas[1][0])