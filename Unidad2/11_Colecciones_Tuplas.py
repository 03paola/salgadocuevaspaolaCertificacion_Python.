#Creando una tupla
coordenadas=(10.5,20.3,30.2)#Tupla numerica
nombres=("Paola","Adriana","Monse")#Tupla str
for indice,coordenadas in  enumerate(coordenadas):
    print(f"[{indice}]coordenadas[{coordenadas}]")
for nombres in nombres:
    print(nombres)
