try:
    #Ejemplo 1 sin manejo de excepciones 
    numero1=int(input("Ingresar el primer numero: "))
    numero2=int(input("Ingresar el segundo numero: "))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("NO SE PUEDE DIVIDIR ENTRE 0")
except ValueError:
    print("SOLO INTRODUCE NUMEROS")
