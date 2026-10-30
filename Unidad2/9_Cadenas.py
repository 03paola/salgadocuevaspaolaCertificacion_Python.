#Cadenas y concatenacion con(+)
cadena1='Hola'
cadena2="Mundo"
multilinea="""Esto es una cadena 
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#Cadenas y repeticion
eco="ja"*5
print(eco)
#Cambiar una cadena de minusculas a mayusculas
tu_nombre='Paola'
print(tu_nombre.upper())
#Cambiar una cadena de mayusculas a minusculas
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#Formato de cadenas (F-String)
edad=15
nombre='Paola'
mensaje=f"Hola,me llamo {nombre} y tengo \n{edad} años"
print(mensaje)
#Contar los caracteres de una cadena
texto="Felicidades por aun continuar en el CECY!!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres) 
#Comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "janva" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido de una cadena
ncadena="aaa794"
print(ncadena.isalpha())
print(ncadena.isdigit())