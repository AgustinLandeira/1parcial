import re 
from os import system
system("cls")

def crear_lista_tipos(lista:list) -> set:
    """
    hace una lista de los tipos de pokemones que hay sin repeticiones
    parametros: recibira una lista(en este caso de pokemon)
    return: retornara un set que seria un conjunto de elementos
    """
    lista_tipos = []
    if len(lista) > 0 and type(lista) == list :
        for pokemon in lista:
            for tipos in pokemon["tipo"]:
                lista_tipos.append(tipos)
            
        lista_unica = set(lista_tipos)
        return lista_unica
    else:
        mensaje = False
        return mensaje
    
def contar_tipos(lista:list,tipo:str) -> int:
    """
    cuenta los tipos de pokemones que haya
    parametros: recibira una lista y el tipo de los pokemones
    return: retornara un int
    """
    contador = 0
    for pokemon in lista:
        for linea in  pokemon["tipo"]:
            if linea == tipo:
                contador +=1
                
                
    return contador

def mostrar_lista_tipos(lista_pokemones):
    """
    mostrara la lista de los tipos con las veces que se repitan
    parametro: recibe una lista
    
    """
    lista_de_tipos = crear_lista_tipos(lista_pokemones)
    
    if type(lista_de_tipos) == set:
        for tipo in lista_de_tipos:
            cantidad = contar_tipos(lista_pokemones,tipo)
            print(f"{tipo} se repite: {cantidad} veces ")
    else:
        print("hubo un error de la lista")

def dividir_segun_tipos(lista:list,tipo:str)->list:
    """
    divide segun el tipo de pokemon y lo agrega a una lista
    parametros: el primer parametro sera la lista y la segunda el tipo de pokemon
    return: retornara una lista
    """
    lista_segun_tipo = []
    if len(lista) > 0 and type(lista) == list:
        for pokemon in lista:
            for linea in pokemon["tipo"]:
                if linea == tipo.capitalize():
                    un_pokemon={}
                    un_pokemon["nombre"] = pokemon["nombre"]
                    un_pokemon["ataque"] = pokemon["ataque"]
                    un_pokemon["tipo"] = pokemon["tipo"]
                    un_pokemon["defensa"] = pokemon["defensa"]
                    
                    lista_segun_tipo.append(un_pokemon)   
                              
        return lista_segun_tipo  
    
def listar_pokemones_por_tipo(lista_pokemon:list):
    """
    va a mostrar una lista con los distintos pokemones que hay junto con su nombre y ataque
    parametro: recibira una lista
    """
    lista_de_tipos = crear_lista_tipos(lista_pokemon)
    if type(lista_de_tipos) == set:
        for tipo in lista_de_tipos:
            
            lista_nombres = dividir_segun_tipos(lista_pokemon,tipo)
            
            print(f"los que tienen {tipo} son:")
            
            for pokemon in lista_nombres:
                print(f"{pokemon['nombre']} y su poder de ataque: {pokemon['ataque']}")
                
            print("***********************************************************************\n")   
            
    else:
        print("hubo un eror en la lista")         

def sacar_promedio(defensa:str,ataque:str)->float:
    """
    saca el promedio entre ataque y defensa del pokemon 
    parametro: recibira el numero ataque y defensa que tenga el  pokemon
    return: retornara el promedio que saco entre la defensa y ataque
    """
    promedio = (int(defensa) + int(ataque)) /2
    
    return promedio
  
def listar_segun_habilidad(habilidad_pedida:str,lista_pokemon:list)->list: 
    """
    busca la habilidad que se le ordeno y la agregara un lista junto con algunos datos
    parametro: recibira una habilidad que ingrese el usuario y una lista de los pokemones
    return: devolvera una lista de los pokemones con su habilidad requerida
    """
    
    cadena = ","
    lista_segun_habilidad = []
    
    if type(habilidad_pedida) == int or  re.match("[0-9]",habilidad_pedida):
        mensaje = None
        return mensaje
    
    else:
        habilidad_pedida = habilidad_pedida.capitalize()
        for pokemon in lista_pokemon:
            
            for habilidad in pokemon["habilidades"]:
                
                if habilidad == habilidad_pedida:
                    
                    un_pokemon={}
                    un_pokemon["nombre"] = pokemon["nombre"]
                    un_pokemon["tipo"] = cadena.join(pokemon["tipo"])
                    un_pokemon["promedio_poder"] = sacar_promedio(pokemon["defensa"],pokemon["ataque"])
                    
                    lista_segun_habilidad.append(un_pokemon)
                    
        return lista_segun_habilidad    

def listar_pokemon_habilidad(descripcion:str,lista_pokemon): 
    """
    muestra una lista de los pokemones con la habilidad que se ha solicitado
    parametro: recibira la descripcion de la habilidad y una lista de pokemones
    """  
    datos = listar_segun_habilidad(descripcion,lista_pokemon)
        
    if datos != None and len(datos) > 0:
            
        for pokemon in datos:
                
            print(f"""
                NOMBRE:{pokemon['nombre']}
                TIPO:{pokemon['tipo']}
                PROMEDIO DE ATAQUE: {pokemon['promedio_poder']}""")
    else:
        print("---------------------------------------------------------------\n")
        print("la habilidad no fue encontrada")
        print("---------------------------------------------------------------\n")    

def ordenar_pokemones(lista_pokemones:list,clave) ->list:
    
    """
    ordena los pokemones por orden de poder
    parametros: recibira la clave que se va a comparar y una lista
    return: retornara una lista  
    """
    
    for i in range(len(lista_pokemones)-1):
        
        for j in range(i+1,len(lista_pokemones)): 
            
            if(int(lista_pokemones[i][clave]) > int(lista_pokemones[j][clave])):
                lista_pokemones[i],lista_pokemones[j] = lista_pokemones[j] ,lista_pokemones[i]
                
            elif int(((lista_pokemones[i][clave])) == int(lista_pokemones[j][clave])):
            
                if(lista_pokemones[i]["nombre"] > lista_pokemones[j]["nombre"]):
                    lista_pokemones[i],lista_pokemones[j] = lista_pokemones[j] ,lista_pokemones[i]
                    
    return lista_pokemones

def listar_pokemones_orden(lista:list,clave:str):
    """
    mostrara el orden de los pokemones
    parametros: recibira una lista y una clave que va ser comparada y ordenada
    """
    
    if len(lista) > 0 and type(clave) == str :
        
        lista_recibida = ordenar_pokemones(lista,clave)
        cadena=","
        for pokemon in lista_recibida:
            print(f"""
            {pokemon["numero_pokedex"]}
            {pokemon["nombre"]} 
            {cadena.join(pokemon["tipo"])}
            {pokemon["ataque"]}
            {pokemon["defensa"]}
            {cadena.join(pokemon["habilidades"])}""")
            
            print("--------------------------------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------------------------------\n")
        print("HUBO UN ERROR\n")
        print("--------------------------------------------------------------------------------------")   
        
def calcular_mayor(ataque:str,defensa:str)->str:
    
    """
    calcula entre los dos cual es mayor o si son iguales
    parametro: recibira el ataque y defensa de un pokemon
    return: retorna cual fue mayor(defensa o ataque)
    """
    
    if int(ataque) > int(defensa):
        
        mensaje = F"{ataque}-ATAQUE"
        
    elif int(defensa) > int(ataque):
        
        mensaje = f"{defensa}-DEFENSA"
        
    else:
        mensaje = f"{ataque}-AMBOS"
    
    return mensaje
    
def guardar_json(path:str,tipo_solicitado:str,lista:list): 
    """
    creara un archivo json  y la guardara
    parametro: path: recibira el nombre del archivo, tipo_solicitado: el tipo del pokemon y una lista
            
    """
    
    import json
    
    if re.match("^[a-zA-Z]+\.json$",path):
        
        un_pokemon = {}
        un_pokemon["tipo"] = []
        
        datos_recibidos = dividir_segun_tipos(lista,tipo_solicitado)
        
        for pokemon in datos_recibidos:
                informacion = calcular_mayor(pokemon["ataque"],pokemon["defensa"])
                
                un_pokemon["tipo"].append({"nombre":pokemon["nombre"],"maximo":informacion})
        
        if un_pokemon["tipo"] == []:     
            print("diccionario vacio")
        else:
            with open(path,"w") as file:
                
                json.dump(un_pokemon,file,indent = 4)
            
    else:
        print("no se pudo entrar")
        
def leer_json(path):
    
    """
    lee el archivo json
    parametro: recibira el nombre del archivo
    """
    import json
    
    with open(path,"r") as archivo:
        diccionario_pokemon = json.load(archivo)
        
    for pokemon in diccionario_pokemon["tipo"]:
        print(f"{pokemon['nombre']}-{pokemon['maximo']}")
    

