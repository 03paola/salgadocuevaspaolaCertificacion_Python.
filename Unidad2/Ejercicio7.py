#El mappa del tesoro
mapa = [
    ["B",".",".","."],
    [".",".",".","."],
    [".",".",".","X"],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Recorriendo la matriz con ciclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):
    #Ciclo externo para manejar columnas(j)
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if mapa[i][j]=="X":
            print(f"Tesoro encontrado en la posicion[{i}][{j}]")
        if mapa[i][j]=="B":
            print(f"Tesoro encontrado en la posicion[{i}][{j}]")
            