def run():
    # for contador in range(50):
        # if contador % 2 != 0:
        #     # Condicional que imprime solo numeros pares
        #     continue
        # # No se va a ejecutar la siguiente instrucción
        # # si el if se cumple, es decir no se va a
        # # imprimir el contador, solo imprime
        # #numeros pares
        # print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    
    texto = input("Escribe un texto:\n")
    for letra in texto:
        if letra == "o":
            break
        print(letra)

if __name__ == "__main__":
    run()