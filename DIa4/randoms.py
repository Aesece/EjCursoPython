from random import *
aleatorio= randint(1,50) ##Retorna un entero aleatorio entre el rango establecido
print(aleatorio)

aleatorio = uniform(1,5) #Retorna un valor decimal que se puede cortar la cantidad de decimales con round
aleatorio = round(uniform(1,5),2)
print(aleatorio)

aleatorio = random() ##Recprta un numero decimal entre 0 y 1
print(aleatorio)

colores=['azul','rojo','verde','naranja'] #Escoge un elemnento aleatorio dentro de una lista
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros) ##Cambia la lista dada como parametro y lo reordena de manera aleatoria
print(numeros)