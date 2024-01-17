def check_3(num):
    return num in range(100,1000)

result = check_3(658)
print(result)

def chk(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False
result=chk([555,99,600])
print(result)

def chk2(lista):
    lista3 = []
    for n in lista:
        if n in range(100,1000):
            lista3.append(n)
        else:
            pass
    return lista3
result=chk2([555,99,600])
print(result)

print(0 in range(1,1000))


##EJEMPLO##

precios_cafe = [('Capuchino',1.5),('Expresso', 2.2),('MOka',1.9)]
for cafe, precio in precios_cafe:
    print(cafe)

#para saber el cafe mas caro
def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

print(cafe_caro(precios_cafe))

cafe, precio = cafe_caro(precios_cafe)

print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")