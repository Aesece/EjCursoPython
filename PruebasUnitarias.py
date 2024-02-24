from random import choice
from pathlib import Path
import os
ruta_recetas = Path(Path.home(), "Recetas")
print(ruta_recetas)
ncat = input("¿Cual sera el nombre de la categoria?\n")
ncat = ruta_recetas / ncat
os.makedirs(ncat)