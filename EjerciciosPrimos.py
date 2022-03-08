def factorial(numero):
       
    if numero == 1:
        return 1
      
    return numero * factorial(numero -1)

def run():
    numero = int(input("Escribe un número:\n"))
    if numero == 1:
        print("No es un número primo")
    else:    
        multiplo = factorial(numero - 1) + 1

        if multiplo % numero == 0:
            print("Es un número primo")
        else:
            print("No es un número primo")

if __name__ == "__main__":
    run()