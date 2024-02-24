from pathlib import Path
base = Path.home()  ##Decuelve una ruta absoluta al directorio principal del usuario actual
guia = Path("Barcelona", "Sagrada.txt")
print(base)
print(guia)
guia = Path(base, "Barcelona", "Sagrada.txt")
print(guia)
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada.txt"))
print(guia)
guia2 = guia.with_name("la_pedrera.txt")
print(guia2)

print(guia.parent.parent)

