colores = ["azul", "morado", "rojo", "amarillo", "negro"]
color = input("Escribe el color: ")
encontrado = False
for contador in colores:
    print(contador)
    #Si el color actual es "rojo", detener el bucle
    if contador==color:
        print("Color encontrado! Saliendo del bucle")
        encontrado=True
        break
if not encontrado:
    print("El color, no se encontro")