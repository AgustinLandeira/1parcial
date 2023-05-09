def traer_csv(path:str)->list:
    import re
    """
    trae los datos de un archivo csv y hace una coleccion
    parametros: recibe un path(nombre del archivo)
    return: retorna la lista
    
    """
    lista_pokemones=[]
    with open(path,"r",encoding="UTF-8") as file:
        for line in file:   
            coleccion={}
            datos=re.split(",|\n",line)
            coleccion["numero_pokedex"] = datos[0]
            coleccion["nombre"] = datos[1]
            coleccion["tipo"] = datos[2].split("/")
            coleccion["ataque"] = datos[3]
            coleccion["defensa"] = datos[4]
            coleccion["habilidades"] = datos[5].replace("Ninguna","").split("|*|")
            
            lista_pokemones.append(coleccion)
    
    return  lista_pokemones
