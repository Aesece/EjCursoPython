monedas= 5
while monedas >0:
    print(f"tengo {monedas} monedas")
    monedas-=1
else:   ###Puede declararse un else en el while cuando la condicion no se cumple
    print("Se acabo el varo")

respuesta = 's'
while respuesta =='s':
    respuesta= input("Quieres seguir? (s/n)")
else:
    print("Gracias")

nombre = input("TU nombre: ")
for letra in nombre:
    if letra == 'r':
        break     ##Termina el ciclo
    print(letra)

for letra in nombre:
    if letra == 'r':
        continue     ##continua el ciclo saltandose esa iteracion
    print(letra)