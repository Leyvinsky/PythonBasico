#Funcioón que realiza la conversión de monedas
def conversor(tipo_peso, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_peso + " tienes? ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas

1- De pesos colombianos a dolares
2- De pesos argentinos a dolares
3- de pesos mexicanos a dolares

Elige una opción:

"""
opcion = int(input(menu))

#PesoColombiano
if opcion == 1:
    conversor("colombianos", 3809.60)
#pesoArgentino
elif opcion == 2:
    conversor("argentinos", 78.31)  
#pesoMexicano
elif opcion == 3:
    conversor("mexicanos", 21.05)
else:
    print("Opción no valida")