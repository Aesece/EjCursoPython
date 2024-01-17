def devolver_distintos(n1, n2, n3):
    lista = [n1, n2, n3]
    suma = sum(lista)
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return  min(lista)
    elif suma >= 10 and suma  <= 15:
        lista.remove(max(lista))
        lista.remove(min(lista))
        return lista.pop()

print(devolver_distintos(2,1,3))


def letras_palabra(palabra):
    mset = set(l for l in palabra)
    lista = list(mset)
    lista.sort()
    return lista

print(letras_palabra('entretenido'))

def verif_ceros(*args):
    aux = -1
    for arg in args:
        valor_actual = arg
        if valor_actual == aux and valor_actual ==0:
            return True
        else:
            aux = valor_actual
    return False

print(verif_ceros(-1,0,5,1,3,3,4,0))

def ceros_vecinos(*args):
     cont =0
     for num in args:
         if cont + 1 == len(args):
             return False
         elif args[cont] == 0 and args[cont + 1] == 0:
             return True
         else:
             cont+=1
     return False
print(ceros_vecinos(-1,0,5,1,3,3,4,0))

def contar_primos(num):
    es_primo = True
    lista =[]
    for n in range(2,num+1):
        if n == 2:
            lista.append(n)
            continue
        else:
            if n % 2 == 0:
                continue
            else:
                for aux in range(3,n,2):
                    if n%aux == 0:
                        es_primo =False
                        break
                    else:
                        es_primo = True
                if(es_primo):
                    lista.append(n)


    return lista

print (contar_primos(100))

def contar_primos(numero):

    primos =[2]
    iteracion = 3

    if numero <2:
        return 0
    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break

        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(100))