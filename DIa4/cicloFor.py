lista = ['a','b','c']

for let in lista:
    n_letra = lista.index(let)+1  ##Para extraer el indice del elemento iterado
    print(f"Letra {n_letra}: {let}")

lista = ['Pablo','Laura','Luis','Julia']
for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print("Nombre sin L")

numeros = [1,2,3,4,5,6,7]
mi_valor=0

for numero in numeros:
    mi_valor+=numero
    print(mi_valor)
print(mi_valor)

palabra = 'Python'
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic={'c1':'a','c2':'b','c3':'c'}
for item in dic:   ##Se imprimen solo las claves
    print(item)
for item in dic.items(): ##Se imprimen los pares con estructura
    print(item)
for item in dic.values(): #Se imprimen solo los valores
    print(item)
for a,b in dic.items():  #Se imprimen los pares de clave y valor en relacion a - b sin estructura
    print(a,b)