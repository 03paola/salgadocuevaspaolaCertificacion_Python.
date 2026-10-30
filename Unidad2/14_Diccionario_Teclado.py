#1. creamos un diccionario
nuevo_usuario={}
#2.Pedimos los datos desde el teclado
nuevo_usuario["Nombre"]= input("Ingresa el nombre: ")
nuevo_usuario["Edad"]= int(input("Ingresa la edad: "))
nuevo_usuario["Estatura"]= float(input("Ingresa tu estatura en metros: "))
print("\n ---Informacion guardada---")
#Mostrando la informacion del diccionario
print(nuevo_usuario)