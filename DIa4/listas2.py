palabra = 'python'

lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

##===es igual a====#

lista = [letra for letra in palabra]
print(lista)

lista = [n for n in range(0,21,2)] #Tambien se puede con numeros
print(lista)

lista = [n/2 for n in range(0,21,2)] #Se pueden aplicar operaciones a cada elemento antes de ingresar a lista
print(lista)

lista = [n for n in range(0,21,2) if n*2 >10] # Influso se pueden validar condiciones para ingresar los eleentos a lista
print(lista)

lista = [n if n*2 > 10 else 'no' for n in range(0,21,2)] ##Pueden agregarse sentemncias else poniendo el bloque al inicio
print(lista)

pies = [10,20,30,40,50]
metros = [round(n / 3.281,2) for n in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [v for v in valores if v%2 == 0 ] ## cuando solo lleva condicion sin else se pone al final
