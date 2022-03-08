def run():
    # los diccionarios se definen con llaves
    mi_diccionario = {
        "llave1": 1, #elementos del diccionario, indice
        "llave2": 2,
        "llave3": 3,
    }

    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina": 449999,
        "Brasil": 23423234,
        "Colombia": 56756756,
    }

    #print(poblacion_paises["Brasil"])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")
    
    

if __name__ == "__main__":
    run()