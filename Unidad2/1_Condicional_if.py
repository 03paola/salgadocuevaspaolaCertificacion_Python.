edad=int(input("Introduce tu edad: "))
if (edad <= 3):
    print("ERES BEBE")
elif edad >= 4 and edad <= 11:
    print("ERES UN NIÑO")
elif edad >= 12 and edad <= 17:
    print("ERES UN ADOLECENTE")
elif edad >= 18 and edad <= 29 :
    print("ERES UN JOVEN")
elif edad >= 30 and edad <= 40:
    print("ERES UN CHAVO-RUCO")
elif edad >= 41 and edad <= 80 :
    print("ERES UN ADULTO")
else:
    print("ESTAS ROBANDO OXIGENO")
