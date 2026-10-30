try:
    alumno=["Paola","Rosalia","Julio","Adriana","Monserrat","Vanessa","Emanuel","Francisco","Maximiliano","Juan Carlos"]
    calificaciones=[9, 8, 10, 7, 9, 8, 10, 6, 9, 10]
    print(alumno[0], calificaciones[0])
    print(alumno[1], calificaciones[1])
    print(alumno[2], calificaciones[2])
    print(alumno[3], calificaciones[3])
    print(alumno[4], calificaciones[4])
    print(alumno[5], calificaciones[5])    
    print(alumno[6], calificaciones[6])
    print(alumno[7], calificaciones[7])
    print(alumno[8], calificaciones[8])

    print("Indices impares: ")
    print(1,3,5,7)
except IndexError:
    print("Error: el indice esta fuera del rango de la lista")
