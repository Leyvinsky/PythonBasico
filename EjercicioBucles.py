#Programa que calcula la tabla de multiplicar de un número cualquiera
def run():
    tabla = int(input("¿Qué tabla de multiplicar deseas conocer?\n\n"))
    for i in range(1,11):
        if i == 11:
            break
        print("\n" + str(tabla*i))

if __name__ == "__main__":
    run()