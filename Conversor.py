opcion = input("Elige que moneda quieres convertir:\n\n1. Pesos Mexicanos a Dólar\n\n2. Dolar a Pesos \n\n")
opcion = int(opcion)
if opcion == 1:
     pesos = input("¿Cuántos pesos tienes? ")
     pesos = float (pesos)
     valordolar = 20.90
     dolares = pesos / valordolar
     dolares = round(dolares, 2)
     dolares = str(dolares)
     print("Tienes $" + dolares + " dólares")

elif opcion == 2:
    dolares = input("¿Cuantos dolares tienes? ")
    dolares = float (dolares)
    valordolar = 20.90
    pesos = dolares * valordolar
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " dólares")

else:
    print("Opción no valida")

