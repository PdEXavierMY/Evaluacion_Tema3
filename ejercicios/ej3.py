import csv
import pathlib

actual_path = pathlib.Path(__file__).parent.absolute()

with open('star_naves.csv', 'r') as file:
    reader3 = csv.DictReader(file, delimiter=';')
    naves_starwars = list(reader3)


def ordenar_naves():
    naves = []
    for fila in naves_starwars:
        naves.append(fila['Name'])
    naves.sort()
    print(f"\n\nLas naves ordenadas por nombre son {naves}")

def ordenar_largo():
    naves_largo = []
    for fila in naves_starwars:
        naves_largo.append(fila['Name'] + " " + fila['Length'])
    naves_largo.sort() ; naves_largo.reverse()
    print(f"\n\nLas naves ordenadas por largo son {naves_largo}")

def millenium_falcon():
    for fila in naves_starwars:
        if fila['Name'] == "Millennium Falcon":
            print(f"\n\nLa información del Halcón Milenario es {fila}")

def estrella_m():
    for fila in naves_starwars:
        if fila['Name'] == "Death Star":
            print(f"\n\nLa información de la Estrella de la Muerte es {fila}")

def cinco_naves():
    naves = []
    for fila in naves_starwars:
        naves.append(fila['Name'] + " " + fila['Passengers'])
    naves.sort()
    naves.reverse()
    print(f"\n\nLas cinco naves con más pasajeros son {naves[:5]}")

def mayor_tripulacion():
    naves = []
    for fila in naves_starwars:
        naves.append(fila['Name'] + " " + fila['Crew'])
    naves.sort()
    naves.reverse()
    print(f"\n\nLa nave que necesita mayor cantidad de tripulación es {naves[0]}")

def comienzan_at():
    at = []
    for fila in naves_starwars:
        if fila['Name'].startswith("AT"):
            at.append(fila['Name'])
    print(f"\n\nLas naves que comienzan con AT son {at}")

def seis_pasajeros():
    pasajeros = []
    for fila in naves_starwars:
        if int(fila['Passengers']) >= 6:
            pasajeros.append(fila['Name'])
    print(f"\n\nLas naves que pueden llevar seis o más pasajeros son {pasajeros}")

def bigger():
    estrella_m = []
    for fila in naves_starwars:
        if fila['Name'] == "Death Star":
            estrella_m.append(fila)
    print(f"\n\nLa información de la nave con mayor largo es {estrella_m}")

def smaller():
    sp_wp = []
    for fila in naves_starwars:
        if fila['Name'] == "SP-Wp":
            sp_wp.append(fila)
    print(f"\n\nLa información de la nave con menor largo es {sp_wp}")
