from random import choice

lista_palabras = ['programa', 'elegir', 'palabra', 'secreta', 'mostrar', 'jugador','solamente', 'serie',
'guiones', 'representa', 'cantidad', 'letras', 'tiene']
palabra = choice(lista_palabras)
lista_guiones = list( '- ' for x in palabra)
lista_incorrectas =[]
letras_ingresadas =[]
vidas = 6
print(".:Bienvenido al juego del ahorcado:.")
print(".:Se ha elegido una palabra al azhar:.\n")

### Funciones #####
def mostrar_palabra_parcial(palabra):
    palabra_guiones = ''
    for l in palabra:
        palabra_guiones += l+' '
    return palabra_guiones
def pedir_letra():
    while True:
        letra = input("Ingresa una letra valida: ")
        if letra.isalpha():
            if letra in letras_ingresadas:
                print("Esa letra ya se ingreso antes, por favor ingresa otra letra a-z")
            else:
                letras_ingresadas.append(letra)
                return letra.lower()
                break
        else:
            print("Letra invalida, por favor ingresa una letra a-z")

def verificar_letra(palabra, letraI, vidas ,listaI, listaG):
    i = 0
    if letraI in palabra:
        print(f"Genial, la letra '{letraI}' se encuentra {palabra.count(letraI)} veces en la palabra")
        for l in palabra:
            if letraI == l:
                listaG[i] = letraI
                i +=1
            else:
                i += 1
    else:
        listaI.append(letraI)
        vidas -= 1
        print(f"Lo siento, la letra '{letraI}' no se encuentra - 1 vida")
        print("Letras incorrectas ingresadas: ")
        print(mostrar_palabra_parcial(listaI))
    return listaG, listaI, vidas

def verificar_palabra_completa(palabra, listaG):
    return palabra == ''.join(listaG)

######JUEGO#######
print(mostrar_palabra_parcial(lista_guiones))
while vidas >0:
    print(" ")
    print(f".:Tienes {vidas} vidas:.")
    letra_ingresada = pedir_letra()
    lista_guiones, lista_incorrectas, vidas = verificar_letra(palabra, letra_ingresada, vidas,lista_incorrectas,lista_guiones)
    print(mostrar_palabra_parcial(lista_guiones))
    if verificar_palabra_completa(palabra, lista_guiones):
        print("Felicidades, Adivinaste la palabra")
        break
if vidas == 0:
    print("Lo siento, te quedaste sin vidas")
    print("La palabra oculta era: "+palabra)





