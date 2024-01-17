dic = {'c1':500,'c2':200}
a = dic.popitem()
print(a)

strs = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
strs = strs.lstrip(",:_#%")
print(strs)


####FUNCIONES####
def saludar_persona(nombre):
    ''' Los comentarios de varias lineas se pueden hacer entre tres comillas simples
    o dobles
    '''
    print("hola " + nombre)

saludar_persona('Carlos')

def mult(n1, n2):
    return n1 * n2

print(mult(4,5))