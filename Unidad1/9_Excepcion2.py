try:
    numero1=int(input("Ingresar el primer numero: "))
    numero2=int(input("Ingresar el segundo numero: "))
    resultado=numero1/numero2
except ValueError:
    print("Solo intoduce numeros")
except ZeroDivisionError:
    print("Division entre cero")
else:
    print("El resultado es:",resultado)
finally:
    print("Programa finalizado")