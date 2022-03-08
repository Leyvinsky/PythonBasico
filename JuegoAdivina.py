import random
# modulo que nos muestra un numero aleatorio, modulo preprogramado de python

def run():
    # random.ranint genera un numero aleatorio del 1 al 100
    numero_aleatorio =  random.randint(1,100)
    numero_elegido = int(input("Elige un número del 1 al 100:\n"))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande\n")
        else:
            print("Busca un número más pequeño\n")
        numero_elegido = int(input("Elige otro número\n"))
    print("\n¡Ganaste!")

if __name__ == "__main__":
    run()