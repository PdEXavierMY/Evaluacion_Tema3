import csv
import pathlib

actual_path = pathlib.Path(__file__).parent.absolute()

with open(str(actual_path) + './star_naves.csv', 'r') as file:
    reader3 = csv.DictReader(file, delimiter=';')
    star_naves = list(reader3)


def ordenar_naves():
    naves = []
    for row in star_naves:
        naves.append(row['Name'])
    naves.sort()
    print(f"\n\nLas naves ordenadas por nombre son {naves}")


def ordenar_largo():
    naves_largo = []
    for row in star_naves:
        naves_largo.append(row['Name'] + " " + row['Length'])
    naves_largo.sort() ; naves_largo.reverse()
    print(f"\n\nLas naves ordenadas por largo son {naves_largo}")

def millenium_falcon():
    for row in star_naves:
        if row['Name'] == "Millennium Falcon":
            print(f"\n\nLa información del Millenium Falcon es {row}")

def death_star():
    for row in star_naves:
        if row['Name'] == "Death Star":
            print(f"\n\nLa información de la Death Star es {row}")

def cinco_naves():
    naves = []
    for row in star_naves:
        naves.append(row['Name'] + " " + row['Passengers'])
    naves.sort() ; naves.reverse()
    print(f"\n\nLas cinco naves con mayor cantidad de pasajeros son {naves[:5]}")

def mayor_tripulacion():
    naves = []
    for row in star_naves:
        naves.append(row['Name'] + " " + row['Crew'])
    naves.sort() ; naves.reverse()
    print(f"\n\nLa nave que requiere mayor cantidad de tripulación es {naves[0]}")

def comienzan_at():
    at = []
    for row in star_naves:
        if row['Name'].startswith("AT"):
            at.append(row['Name'])
    print(f"\n\nLas naves que comienzan con AT son {at}")

def seis_pasajeros():
    pasajeros = []
    for row in star_naves:
        if int(row['Passengers']) >= 6:
            pasajeros.append(row['Name'])
    print(f"\n\nLas naves que pueden llevar seis o más pasajeros son {pasajeros}")
