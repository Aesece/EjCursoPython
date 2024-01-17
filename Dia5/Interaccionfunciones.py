from random import shuffle
# Lista inicial
palitos = ['=','==','===','====']
#Funcion mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista
#soliciotar intento al usuario
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4")

    return int(intento)
#comprobar el intento
def comprobar(lista, intento):
    if lista[intento-1] == '=':
        print("Perdiste")
    else:
        print("Esta vez te salvaste")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar(palitos_mezclados, seleccion)