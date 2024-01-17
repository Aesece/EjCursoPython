from random import randint
ran = randint(1,101)

print(".:Bienvenido al juego de adivinar un numero:.")
player = input("Ingresa el nombre del jugador: ")
print(f"Bueno {player}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

intento = 1
while intento <=8:
    num = input("Ingresa un numero:")
    if not num.isnumeric():
        if intento == 8:
            print(f"Has perdido, gastaste los 8 intentos, el numero era {ran}")
        else:
            print("Caracter no permitido, ingresar numero del 1 - 100")
        intento += 1

        continue
    num = int(num)
    if num not in (range(1,101)):
        print("Numero fuera de rango, ingresar numero del 1 - 100")
        if intento == 8:
            print(f"Has perdido, gastaste los 8 intentos, el numero era {ran}")
    elif num < ran:
        if intento == 8:
            print(f"Has perdido, gastaste los 8 intentos, el numero era {ran}")
        else:
            print("EL numero que ingresaste es menor que el que pense, intenta otra vez")
    elif num > ran:
        if intento == 8:
            print(f"Has perdido, gastaste los 8 intentos, el numero era {ran}")
        else:
            print("EL numero que ingresaste es mayor que el que pense, intenta otra vez")
    else:
        print(f"CORRECTO!!! Felicidades {player}, adivinaste el numero, te tomo {intento} intentos")
        break
    intento+=1
