from random import randint
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self. nombre} {self.apellido} \n Numero de cuenta {self.numero_cuenta} \n Balance: {self.balance}"
    def retirar(self, cantidad) -> bool:
        if self.balance < cantidad:
            return False
        else:
            self.balance = self.balance - cantidad
            return True

    def depositar(self, cantidad) -> bool:
        if cantidad > 0:
            self.balance = self.balance + cantidad
            return True
        else:
            return False





####MAIN####
def crear_cliente(nombre, apellido):
    n_cuenta = randint(1000, 9999)
    cuenta = Cliente(nombre, apellido, n_cuenta, 0.0)
    return cuenta

def inicio():
    print("Banco Python")
    nombre = input("Ingrese su nombre(s)")
    apellido = input("Ingrese su apellido")
    cuenta_cliente = crear_cliente(nombre, apellido)
    print("Se ha creado su cuenta: ")
    print(cuenta_cliente)
    while True:
        opcion = 'x'
        while opcion.isnumeric():
            print("Opciones de accion:")
            print("[1] Consultar informacion de la cuenta")
            print("[2] Depositar ")
            print("[3] Retirar")
            print("[4] Salir")
            opcion = input("Selecciona una opcion")
        match opcion:
            case 1:
                print(cuenta_cliente)
            case 2:
                cantidad = input("Ingresa la cantidad a depositar")
                cuenta_cliente.depositar(cantidad)



