class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

    def  hablar(self):
        print("Este animal emite un sonido")
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print("Pio")
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolon = Pajaro(2, "Amarillo",60)
piolon.nacer()
print(piolon.color)
print("")
piolon.hablar()
piolon.volar(20)
### Herencia extendida#
mi_animal = Animal(5, "negro")
print("")

class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("jajajja")
    def hablar(self):
        print("que tal")

class Hijo(Padre, Madre):  #Heredara primero de Padre
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)