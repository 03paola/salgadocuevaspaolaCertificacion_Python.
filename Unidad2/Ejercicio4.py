promedio = [9,8,7,10,5]
#Encontrar el promedio mas bajo usando un ciclo for
#Suponemos inicialmente que el promedio mas bajo es el primer elemento
promedio_bajo = promedio[0]
promedio_alto = promedio[0]
for contador in promedio:
    if contador < promedio_bajo:
        promedio_bajo=contador
    if contador > promedio_alto:
        promedio_alto=contador
print(promedio_alto)
print(promedio_bajo)