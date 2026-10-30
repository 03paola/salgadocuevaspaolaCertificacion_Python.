abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
filas = 3
columnas = 9
matriz = []
for i in range(filas):
    fila = ""
    for j in range(columnas):
        fila += abecedario[i * columnas + j]
    matriz.append(fila)
for fila in matriz:
    print(fila)