#Son listas de pares con relacion clave-valor
#No son ordenadas
#se delcaran con llaves
#las claves deben de se runicas, valores pueden repetirse
diccionario={'c1':'valor1','c2':'valor2'}
print(type(diccionario))

print(diccionario)

res=diccionario['c1'] #se busca mediante clave
print(res)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.73}
res=cliente['talla']
print(res)

#puede contener claves con valores de cualquier tipo incluyendo listas u otros diccionarios
dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200},'c4':'Hola'}
print(dic['c2'])
print(dic['c2'][2])
print(dic['c3'])
print(dic['c3']['s1'])

dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
letra=(dic2['c2'][1]).upper()
print(letra)

dic3 = {1:'a',2:'b'}
print(dic3)

dic3[3]='c'
print(dic3)

dic3[2]='B'
print(dic3)

print(dic3.keys())
print(dic3.values())
print(dic3.items())


