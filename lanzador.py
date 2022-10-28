import re
from ejercicios import ej1, ej2, ej3, ej4, ej5

def ejecutar():
    eleccion = int(input("Elige el ejercicio a ejecutar: "))
    if eleccion == 1:
        a1=ej1.primera_aguja;a2=ej1.segunda_aguja,a3=ej1.tercera_aguja
        ej1.pila_a_pila(a1,a2)
        ej1.pila_a_pila(a2,a3)
        print(a3.items)
    elif eleccion == 2:
        rec_it = int(input("¿Determinante recursivo(1) o iterativo(2)?: "))
        if rec_it == 1:
            mat = ej2.construir_matriz_recursivo()
            print(mat); print(ej2.regla_de_sarrus(mat))
        elif rec_it == 2:
            mat = ej2.construir_matriz_iterativo()
            print(mat); print(ej2.regla_de_sarrus(mat))
    elif eleccion == 3:
        ej3.ordenar_naves()
        ej3.ordenar_largo()
        ej3.millenium_falcon()
        ej3.estrella_m()
        ej3.cinco_naves()
        ej3.mayor_tripulacion()
        ej3.comienzan_at()
        ej3.seis_pasajeros()
        ej3.bigger()
        ej3.smaller()

    elif eleccion == 4:
        pass
    elif eleccion == 5:
        mensaje = input('Ingrese el mensaje a encriptar: ')
        encriptacion = ej5.Encripta(mensaje)
        print(encriptacion.encriptar())