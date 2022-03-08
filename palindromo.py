#Definición de la función de palindromo, antes de la función run
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else: 
        return False

#Definición de la función Run y llamado de función palindromo
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Invocación de la función principal run
if __name__ == "__main__":
    run()
