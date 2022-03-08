def conversacion(mensaje):
    print("Hola")
    print("¿Cómo estás?")
    print(mensaje)
    print("Adios")
    
opcion = int(input("Elige un opción\n1\n2\n3\n"))

if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else: 
    print("Escribe una opción incorrecta")


def suma(a, b):
    print("Función que suma dos números")
    resultado = a + b
    return resultado

sumatoria = suma(1,4)

print(sumatoria)

