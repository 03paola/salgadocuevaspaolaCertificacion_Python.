#Creando una matriz
matriz=[
    [5,8,1],#Fila 1 x 3 columnas
    [3,9,2]#Fila 2 x 3 columnas
]
#Obteniendo el número total de filas y columnas
filas=len(matriz)
columnas=len(matriz[0])
#Ciclo externo para los indices de las filas
for i in range(filas):
    #Ciclo interno para los indices de las columnas
    for j in range(columnas):
        print(f"Posicion[{i}][{j}]={matriz[i][j]}")