##Es lo equivalente el switch
serie = "N-02"
match serie:
    case "N-01":
        print("Smsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("MOtorola")
    case _:
        print("No existe producto")

##Se pueden hacer match o selector de casos aplciados a una estructura
cliente= {'nombre':'Carlos',
          'Edad':27,
          'Ocupacion':'QA'
          }
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica':{'protagonista':'Keanu Reaves',
                             'directos':'Lana wasdas'
                             }
            }
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,'Edad':edad,'Ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,'directos':director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se detecta")