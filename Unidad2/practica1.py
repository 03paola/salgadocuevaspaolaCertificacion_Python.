alumnos = ["Paola","Monse","Adriana","Rosalia","Maximiliano","Emmanuel","Vanessa","Julio","Francisco","Juan Carlos"]
promedio = []
for nombre in alumnos:
    calificacion = float(input("Ingresa el promedio de"+ nombre+ ":"))
    promedio.append(calificacion)
promedio_alto = promedio[0]
promedio_bajo = promedio[0]
alumno_alto = alumnos[0]
alumno_bajo = alumnos[0]
print("\nPROMEDIO DE CADA ALUMNO")
for i in range(8):
    print(alumnos[i], ":", promedio[i])
    if promedio[i] > promedio_alto:
        promedio_alto = promedio[i]
        alumno_alto = alumnos[i]

    if promedio[i] < promedio_bajo:
        promedio_bajo = promedio[i]
        alumno_bajo = alumnos[i]
print("\nPromedio más alto:", alumno_alto, promedio_alto)
print("Promedio más bajo:", alumno_bajo, promedio_bajo)