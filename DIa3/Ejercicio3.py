texto=(input("Ingrese un texto:")).lower()
print("Ahora ingrese 3 letras")
letras=[]
letras.append(input("Letra 1: ").lower())
letras.append(input("Letra 2: ").lower())
letras.append(input("Letra 3: ").lower())

print(f"\nLa letra \"{letras[0]}\" aparece {texto.count(letras[0])} veces")
print(f"La letra \"{letras[1]}\" aparece {texto.count(letras[1])} veces")
print(f"La letra \"{letras[2]}\" aparece {texto.count(letras[2])} veces \n")

palabras = texto.split()

print(f"El texto ingresado tiene {len(palabras)} palabras \n")
print(f"La primera letra del texto es: \"{texto[0]}\" y la ultima lerta es: \"{texto[len(texto)-1]}\" \n")
print(f"El texto invertido es:")
palabras.reverse()
print(" ".join(palabras))

dic = {True: "si", False: 'no'}
control= "python" in palabras

print(f"\nLa palabra Python {dic[control]} se encuentra en el texto ingresado")