if 1>9:
    print("es correcto")
else:
    print("NO es correcto")

mascota = 'perro'
if mascota == "gato":
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
elif mascota == 'pez':
    print("pez")
else:
    print("No se que animal tienes")

edad=16
calificacion=8
if edad<18:
    print("eres menor de edad")
    if calificacion >=7:
        print("aprobado")
    else:
        print("No aprobado")
else:
    print("Eres mayor")

habla_ingles = True
sabe_python = True
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")