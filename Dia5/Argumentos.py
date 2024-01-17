def suma(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

print(suma(5,6))

 ####   KWARGS ####3
def suma(**kwargs):

    total = 0
    for clave, valor in kwargs.items():
       print(f"{clave} = {valor}")
       total += valor
    return total
suma(x=3,y=5,z=3)


def prueba(num1, num2, *args, **kwargs):

    print(f"el primer valor es {num1}")
    print(f"el primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
       print(f"{clave} = {valor}")

prueba(15,50, 50,30,40, 5, x=3,y=5,z=3)

