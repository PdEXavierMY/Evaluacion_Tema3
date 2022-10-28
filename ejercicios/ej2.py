def construir_matriz_iterativo():
    matriz = [[], [], []]
    for i in range(3):
        for i in range(3):
            numero = int(input("Introduce un elemento de la matriz(por columnas): "))
            matriz[i].append(numero)
    return matriz

def construir_matriz_recursivo(n=0, fila=0, matriz=[[], [], []]):
    if fila < 3:
        if n < 3:
            numero = int(input("Introduce un elemento de la matriz(por filas): "))
            matriz[fila].append(numero)
            construir_matriz_recursivo(n+1, fila, matriz)
        else:
            numero = int(input("Introduce un elemento de la matriz(por filas): "))
            matriz[fila].append(numero)
            construir_matriz_recursivo(0, fila+1, matriz)
    else:
        return matriz

def regla_de_sarrus(matriz):
    return int((matriz[2][2]*matriz[1][1]*matriz[0][0])+(matriz[1][2]*matriz[0][1]*matriz[2][0])+(matriz[2][1]*matriz[1][0]*matriz[0][2])-(matriz[2][0]*matriz[1][1]*matriz[0][2])-(matriz[2][1]*matriz[1][2]*matriz[0][0])-(matriz[1][0]*matriz[0][1]*matriz[2][2]))

ca = construir_matriz_recursivo()
print(ca)