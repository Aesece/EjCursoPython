from pathlib import Path, PurePath
import os
import shutil
from os import system
ruta_recetas = Path(Path.home(), "Recetas")
print(ruta_recetas)
categorias = []
recetas = []
contador = 0

def contar_recetas():
    return len([obj for obj in Path(ruta_recetas).glob("**/*.txt")])


###FUNCIONES PRINCIPALES###
def leer_receta():
    print("Existen las siguientes categorias: ")
    ruta_base = seleccionar_cat()
    print("En la categoria seleccionada estan las recetas: ")
    archivo_rec = seleccionar_receta(ruta_base)
    if not archivo_rec:
        pass
    else:
        file = open(archivo_rec, "r")
        print(file.read())
        file.close()
        print("\n")

def crear_receta():
    print("¿De que categoria sera la nueva receta? ")
    ruta_base = seleccionar_cat()
    existe = True
    while existe:
        nombre_receta = input("¿Cual sera el nombre de la receta?\n")+".txt"
        archivo = ruta_base/nombre_receta
        if os.path.exists(archivo):
            existe = True
            print("La receta que intentas crear ya existe, elige otro")
        else:
            existe = False

    descripcion = input("Describe la receta: \n")
    Path.write_text(archivo, descripcion)
    print(f'La receta "{archivo.stem}" se ha creado y añadido al menu')
    print("\n")

def crear_categoria():
    existe=True
    print("Se creara una nueva categoria de recetas")
    while existe:
        ncat = input("¿Cual sera el nombre de la categoria?\n")
        rcat = ruta_recetas / ncat
        if os.path.exists(rcat):
            existe = True
            print("La categoria que intentas crear ya existe, elige otro")
        else:
            existe = False

    os.makedirs(rcat)
    print(f'Se ha creado la nueva categoria "{ncat}" \n')
def eliminar_receta():
    print("Selecciona la categoria de la receta: ")
    ruta_base = seleccionar_cat()
    print("En la categoria seleccionada estan las recetas: ")
    archivo_rec = seleccionar_receta(ruta_base)
    if not archivo_rec:
        pass
    else:
        os.remove(archivo_rec)
        print(f"Se ha eliminado la receta '{archivo_rec.stem}'\n")


def eliminar_catgoria():
    print("Actualmente se tienen las siguientes cateorias")
    ruta_base = seleccionar_cat()
    cat = os.path.basename(os.path.normpath(ruta_base))
    conf = input(f'La categoria "{cat}" podria contener recetas, ¿Estas seguro de eliminar? s/n : ').lower()
    if conf == 's':
        shutil.rmtree(ruta_base)
        print("Se ha eliminado la categoria con todo su contenido\n")
    else:
        print('\n')


###FUNCIONES SECUNDARIAS###
def seleccionar_cat():
    contador = 0
    categorias = next(os.walk(ruta_recetas))[1]
    for cat in categorias:
        print(f"{contador+1} : {cat}")
        contador += 1

    cat_selec = 'x'
    while not cat_selec.isnumeric() or int(cat_selec) not in range(1, len(categorias)+1):
        cat_selec = input("Selecciona una:")
    cat_selec = int(cat_selec)-1
    ruta_cat_sel = Path(ruta_recetas, categorias[cat_selec])
    print(ruta_cat_sel)
    return ruta_cat_sel

def seleccionar_receta(cat):
    contador = 0
    recetas = [txt for txt in Path(cat).glob("*.txt")]
    if len(recetas) == 0:
        print("Lo siento, aun no hay recetas en esta categoria\n")
        return False
    else:
        for rec in recetas:
            print(f"{contador + 1} : {rec.stem}")
            contador += 1
        rec_selec = 'x'
        while not rec_selec.isnumeric() or int(rec_selec) not in range(1, len(recetas) + 1):
            rec_selec = input("Selecciona una: ")

        rec_selec = int(rec_selec) - 1
        ruta_rec_sel = recetas[rec_selec]
        print(ruta_rec_sel)
        return ruta_rec_sel

def menu_accion():
    opcion = 'x'
    while not opcion.isnumeric():
        print("\nOpciones de accion:")
        print("[1] Leer Receta")
        print("[2] Crear Receta")
        print("[3] Crear categoria")
        print("[4] Eliminar Receta")
        print("[5] Eliminar categoria")
        print("[6] Finalizar programa")
        opcion = input("\nSelecciona una opcion:")
    return opcion


##############PROGRAMA###########
while True:
    print("*" * 50)
    print("*" * 6 + " Hola bienvenido al gestor de recetas " + "*" * 6)
    print("*" * 50)
    print(f"Las recetas se encuentran en {ruta_recetas}")
    print(f"Actualmente tienes {contar_recetas()} recetas en total")
    opcion = int(menu_accion())

    match opcion:
        case 1:
            leer_receta()
        case 2:
            crear_receta()
        case 3:
            crear_categoria()
        case 4:
            eliminar_receta()
        case 5:
            eliminar_catgoria()
        case 6:
            print("Hasta luego...")
            break
        case _:
            print("Opcion no valida o no definida, por favor selecciona una opcion valida \n")


