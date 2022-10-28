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

