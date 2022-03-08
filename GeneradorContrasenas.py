import random

def generar_contrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f","g"]
    simbolos = ["!", "#", "$", "&", "/", "(", ")"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        #choice elije un caracter al azar para asignarlo a caractare random
        caracter_random = random.choice(caracteres)
        #le agrega el caracter random a la lista contraseña
        contrasena.append(caracter_random)

        #convierte a string la cadena original
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es:\n" + contrasena)


if __name__ == "__main__":
    run()
