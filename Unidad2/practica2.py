dias_permitidos = ("lunes","miercoles","viernes")
dia_ingresado = input("Ingresar el dia de la semana para la solicitud: ")
if dia_ingresado in dias_permitidos:
    print("Solicitud permitida")
else:
    print("No hay atencion ese dia")