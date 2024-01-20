from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\QA\\Documents\\Curso Python\\Projects\\PrimerProyecto\\Dia6\\prueba.txt')
ruta_windows = PureWindowsPath(carpeta) ##Convierte una ruta en una ruta de windows

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("No existe")
else:
    print("Simon existe")

