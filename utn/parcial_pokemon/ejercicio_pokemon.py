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

def mostrar_lista_tipos(lista_pokemones):#2
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
    
def listar_pokemones_por_tipo(lista_pokemon:list):#3
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

def listar_pokemon_habilidad(descripcion:str,lista_pokemon):#4
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

def listar_pokemones_orden(lista:list,clave:str):#5
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
    
def guardar_json(path:str,tipo_solicitado:str,lista:list): #6
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
            print("no se encontro el tipo")
        else:
            with open(path,"w") as file:
                
                json.dump(un_pokemon,file,indent = 4)
            
    else:
        print("no se pudo entrar")
        
def leer_json(path): #7
    
    """
    lee el archivo json
    parametro: recibira el nombre del archivo
    """
    import json
    
    with open(path,"r") as archivo:
        diccionario_pokemon = json.load(archivo)
        
    for pokemon in diccionario_pokemon["tipo"]:
        print(f"{pokemon['nombre']}-{pokemon['maximo']}")
 
def agregar_pokemon(lista_recibida:list)->list: # 8
    
    """
    agregara un pokemon a la lista si es que no se repite
    parameters: recinira una lista de pokemones
    return : devolvera una lista con o sin nuevos pokemones
    """

    while True:
        
        lista_tipos = []
        lista_habilidades = []
        
        repetido = False
        
        un_pokemon = {}
        
        un_pokemon["numero_pokedex"] = input("ingrese el numero de pokedex: ")
        
        while un_pokemon["numero_pokedex"] == "" or re.match("[a-zA-Z]",un_pokemon["numero_pokedex"]):
            un_pokemon["numero_pokedex"] = input("error,ingrese el numero de pokedex: ")
             
        un_pokemon["nombre"] = input("ingrese el nombre: ")
        
        while un_pokemon["nombre"] == "" or re.match("[0-9]",un_pokemon["nombre"]):
            un_pokemon["nombre"] = input("error,ingrese el nombre del pokemon : ")
        
        while True:
            
            un_pokemon["tipo"] = input("ingrese el tipo de pokemon: ").capitalize()
            
            while un_pokemon["tipo"] == "" or re.match("[0-9]",un_pokemon["tipo"]):
                un_pokemon["tipo"] = input(" error, ingrese el tipo de pokedex: ")
            
            respuesta = input("desea ingresar otro tipo?: ")
            
            while respuesta != "no" and respuesta != "si":
                respuesta = input("desea ingresar otro tipo?: ")
                
            lista_tipos.append(un_pokemon["tipo"])
            
            if respuesta == "no":
                break
                
        un_pokemon["ataque"] = input("ingrese el  poder de ataque del pokemon: ")
        
        while re.match("[a-zA-Z]",un_pokemon["ataque"]) or un_pokemon["ataque"] == "":
            
            un_pokemon["ataque"] = input("ERROR,ingrese el  poder de ataque del pokemon: ")
        
        un_pokemon["defensa"] = input("ingrese el poder de defensa: ")
        
        while re.match("[a-zA-Z]",un_pokemon["defensa"]) or un_pokemon["defensa"] == "":
            un_pokemon["defensa"] = input("ERROR,ingrese el poder de defensa: ")
            
        while True:
            
            un_pokemon["habilidades"] = input(" ingrese las habilidades del pokemon: ").capitalize()
            
            while re.match("[0-9]",un_pokemon["habilidades"]) or un_pokemon["habilidades"] == "":
                un_pokemon["habilidades"] = input("porfavor ingreser la habildad?: ")
                 
            respuesta = input("desea ingresar otra habilidad?: ")
            
            while respuesta != "no" and respuesta != "si":
                respuesta = input("desea ingresar otra habildad?: ")
            
            lista_habilidades.append(un_pokemon["habilidades"])
            
            if respuesta == "no":
                break
            
        un_pokemon["habilidades"] = lista_habilidades
        un_pokemon["tipo"] = lista_tipos
        
        for pokemon in lista_recibida:
            if pokemon["nombre"] == un_pokemon["nombre"]:
                print("el pokemon ya existe")
                repetido = True
                break
            
        if repetido != True:
            lista_recibida.append(un_pokemon)
            print(lista_recibida)
        
        respuesta = input("desea ingresar un nuevo pokemon? ")
        
        while respuesta != "si" and respuesta != "no":
            respuesta = input("ERROR,desea ingresar un nuevo pokemon?(SI O NO):  ")
        
        if respuesta == "si":
            continue
        else:
            break
         
    return lista_recibida    
    
def guardar_datos_csv(lista_recibida:list): #9
    """
    guarda datos en un nuevo csv
    parametros: va a recibir una lista de pokemones
    """
    
    with open("nuevoo.csv","w",encoding="UTF-8") as file:
        
        for pokemon in lista_recibida:
            
            pokedex = pokemon["numero_pokedex"]
            nombre = pokemon['nombre']
            
            tipo = pokemon['tipo']
            
            if len(tipo) >1:
                cadena = "/"
                tipo = cadena.join(tipo)
            else:
                cadena =""
                tipo = cadena.join(tipo)
            
            ataque = pokemon['ataque']
            defensa = pokemon['defensa']
            habilidades = pokemon['habilidades']
            
            for i in range(len(habilidades)):
                if habilidades[i] == "":
                    habilidades[i] = "Ninguna"
            
            if len(habilidades) >1:
                cadena = "|*|"
                habilidades = cadena.join(habilidades)
            else:
                cadena = "|*|Ninguna"
                habilidades = cadena.join(habilidades)
            
            line = f"{pokedex},{nombre},{tipo},{ataque},{defensa},{habilidades}\n"
            file.write(line)

def contar_pokemon_eliminado(lista_filtrada:list)->int:
    """
    va a contar la lista_filtrada de los pokemones que cumplieron con la condicion pedida
    parametro: recibe la lista de pokemones que coincidieron con la busqueda
    return : devulve un contador de cuantos pokemones se va a eliminar
    """
    contador = 0
    for i in range(len(lista_filtrada)):
        contador += 1
        
    return contador

def buscar_pokemon(criterio,lista_pokemon:list,campo_buscado:str):
    """
    busca el pokemon con el campo solicitado
    parametro: recibe la condicion, la lista de pokemones y el campo que seria una clave
    return: retorna una lista de pokemnes sin los que coincidieron con el criterio y un contador de los que
    fueron eliminados
    """
    lista_filtrada = []
    
    agua = 0
    
    for pokemon in lista_pokemon:#for valor in pokemon[campo_buscado]:
        
        if type(pokemon[campo_buscado]) == list:
            
            for elemento in pokemon[campo_buscado]:
        
                if criterio(elemento):
                    agua += 1
                    lista_filtrada.append(pokemon)         
                                        
        elif criterio(pokemon[campo_buscado]):
            
            lista_filtrada.append(pokemon)
    
    for pokemon in lista_filtrada:
        lista_pokemon.remove(pokemon)   
    
    contador = contar_pokemon_eliminado(lista_filtrada)
    
    if contador == 0:
        contador = "no se encontro ninguna pokemon que cumpla con la condicion"   
              
    return lista_pokemon,contador
    
def mostrar_pokemones_eliminados(lista_pokemon,campo,valor):#10
    
    existe_campo = False
    
    for clave in lista_pokemon:
        if campo in clave:
            existe_campo = True
            
    if existe_campo:
        lista_pokemon,informe = buscar_pokemon(lambda pokemon: pokemon == str(valor).capitalize(),lista_pokemon,campo)
    else:
        informe = "no existe el campo"
   
    print(f"""
        campo: {campo}
        valor: {valor}
        informe: la cantidad de pokemones eliminados fueron: {informe} """)
#
def agregar_ceros(pokedex:str,cantidad:int):
    """
    agrega los ceros necesarios para completar los 12 caracteres
    parametros: recibe el pokedex y la cantidad de caracteres que hay en el codigo
    return: retorna los ceros que se necesitaban con el numero de pokedex
    """
    ceros_necesarios = 12 - cantidad
    
    pokedex = pokedex.zfill(ceros_necesarios)
    return pokedex

def calcular_valor_alto(valor_1:str,valor_2:str)->str:
    """
    calcula el mayor de los valores de dos campos
    parametro: recibe dos valores de dos campos distintos para comparar
    return: el mayor valor de los campos o empate y su campo
    """
    campo_alto = "ninguno"
    mayor_valor = "ninguno"
    
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
    
    if type(valor_1) == int and type(valor_2) == int:
        
        if valor_1 > valor_2:
            campo_alto = "a"
            mayor_valor = valor_1
            
        elif valor_1 < valor_2:
            campo_alto = "d"
            mayor_valor = valor_2
        
        else:
            campo_alto = "ad"
            mayor_valor = valor_1
            
    return campo_alto,mayor_valor
    
def obtener_inicial_nombre(pokemon:str)->str:
    """
    agarra la inicial de los nombres de los pokemones
    parametro: recibe el nombre del pokemon
    return: la inicial del nombre
    """
    nombre_pokemon = pokemon
    
    return nombre_pokemon[0]
    
def generar_codigo_pokemon(pokemon:dict)->str: 
    """
    va a generar el codigo de cada pokemon en la lista
    parametro: recibe un diccionario que seria un pokemon
    return: retornara un mensaje de 12 caracteres con su inicial,campo mas alto con su valor y pokedex
    """
    
    inicial = obtener_inicial_nombre(pokemon['nombre'])
    
    campo_alto,valor_alto = calcular_valor_alto(pokemon["ataque"],pokemon["defensa"])
    
    mensaje = f"{inicial}-{campo_alto.upper()}-{valor_alto}-"
    
    pokedex_con_ceros = agregar_ceros(pokemon["numero_pokedex"],len(mensaje))
    mensaje = f"{inicial}-{campo_alto.upper()}-{valor_alto}-{pokedex_con_ceros}"
    
    return mensaje
    
#
def agregar_codigos_pokemon(lista_pokemones:list): #11
    """"
    agrega el codigo a cada uno de los pokemones de la lista
    parametro: recibe la lista de pokemones
    """
    for pokemon in lista_pokemones:
        codigo = generar_codigo_pokemon(pokemon)
        pokemon["codigo"] = codigo
        
    for pokemon in lista_pokemones:
        print(f"el pokemon se llama: {pokemon['nombre']} y su codigo es : {pokemon['codigo']}")
    
     

