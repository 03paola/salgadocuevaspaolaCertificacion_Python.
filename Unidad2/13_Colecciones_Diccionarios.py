persona={
    "nombre":"Paola",
    "edad":16,
    "profesion":"Ingenieria en sistemas",
    "estudiante":True
}
print(persona)
#Accediendo a un valor en especifico
print(persona["profesion"])
#Se puede usar el metodo .get()
#Es util porque no da error si la clave no existe
print(persona.get("edad"))
#Modificar un valor existente 
persona["edad"]=16
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="San pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"{clave}:{valor}")