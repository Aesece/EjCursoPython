##Une dos o mas listas en una lista de tuplas conformada por los pares formados de un elemento de cada lista
#LLega hasta el largo de la lista mas corta
nombres= ['AnA','Hugo','Valreroa']
edades=[65,29,72]
ciudades=['Lima','Madrid','Mexico']

comb= list(zip(nombres,edades,ciudades))
print(comb)

for nombre,edad,ciudad in comb:
    print(f"{nombre} tiene {edad}y vive en {ciudad}")

espanol = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']

numeros=list(zip(espanol,portugues,ingles))
print(numeros)