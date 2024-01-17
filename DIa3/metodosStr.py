texto= "Este es el texto de Carlos"

res=texto
print(res)

res=texto.upper() #Mayusculas
print(res)

res=texto[2].upper() #Permite indices
print(res)

res=texto.lower() #Minusculas
print(res)

res=texto.split("t") #Separa en una lista de cadenas segun el parametro
print(res)

a="Aprender"
b="Python"
c="esta"
d="esta prron"

e=" -".join([a,b,c,d])  #Une elementos de una lista segun el cliterio de la cadena
print(e)


res=texto.find("g") #Encuentra el indice donde aparece el texto o cadena ingresada, devuelve -1 cuando no encuentra nada
print(res)

res=texto.replace("Carlos","todos") #Reemplaza caracter o cadena por la cadena dadaUp
print(res)