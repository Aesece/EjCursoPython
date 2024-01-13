nombre = input("Ingresa tu nombre: ")
ventas= int(input("Ingresa tus ventas: "))

comision=round(((ventas*13)/100),2)

print(f"Las ventas del empleado: {nombre} son {ventas} y su comision es de: {round(((ventas*13)/100),2)}")