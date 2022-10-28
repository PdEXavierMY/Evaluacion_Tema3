import re
from ejercicios import ej1, ej2, ej3, ej4, ej5

def ejecutar():
    eleccion = int(input("Elige el ejercicio a ejecutar: "))
    if eleccion == 1:
        ej1.ejecutar()
    elif eleccion == 2:
        rec_it = int(input("¿Determinante recursivo(1) o iterativo(2)?: "))
        if rec_it == 1:
            mat = ej2.construir_matriz_recursivo()
            print(mat); print(ej2.regla_de_sarrus(mat))
        elif rec_it == 2:
            mat = ej2.construir_matriz_iterativo()
            print(mat); print(ej2.regla_de_sarrus(mat))
    elif eleccion == 3:
        ej3.ejecutar()
    elif eleccion == 4:
        ej4.ejecutar()
    elif eleccion == 5:
        mensaje = input('Ingrese el mensaje a encriptar: ')
        encriptacion = ej5.Encripta(mensaje)
        print(encriptacion.encriptar())