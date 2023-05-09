
from Data_stark import lista_personajes
from os import system
system("cls")

def mostrar_datos_normalizados():
    """
    muestra los datos normalizados de la lista
    """
    mostrar=stark_normalizar_datos(lista_personajes)
    print(f"{mostrar}")

def stark_normalizar_datos(lista:list):
    """
    Brief: Normaliza los datos de la lista es decir convierte en dato correcto las keys
    Parameters:
        lista: lista de personajes
        return: devuelve los datos normalizados
    """
    mensaje=None
    if len(lista_personajes) != 0:
        
        for heroe in lista:
            if type(heroe['altura']) == str or type(heroe['peso']) ==str or  type(heroe['fuerza']) !=int:
                
                heroe['altura']=float(heroe['altura'])
                heroe['peso'] = float(heroe['peso'])
                heroe['fuerza']=int(heroe['fuerza'])
            #print(lista)
            mensaje="datos normalizados"  
    else:
        mensaje="ERROR la lista esta vacia"
        
    return mensaje   

def obtener_nombre(superheroe:dict):
    """
    brief:devuelve el nombre del superheroe
    parameters: RECIBE UN DICCIONARIO DE LA LISTA
    
    """
    if dict != None:
        return f"Nombre: {superheroe['nombre']}"
        
def imprimir_dato(dato:str):
    """
    brief :muestra un mensaje solo si es una  cadena
    parameters: un dato en cadena 

    """
    if type(dato) == str :
        print(dato)

def stark_imprimir_nombres_heroes(lista:list): 
    """
    brief:  recorre la lista y muestra los nombres de esa lista que le pasen
    parameters: 
    lista: lista de superheroes
    """
    
    
    retorno = -1 
    
    if len(lista) >0 :
        for heroe in lista:
            imprimir_dato(obtener_nombre(heroe))
            imprimir_dato("\n----------------------------------------------\n")
            #print(obtener_nombre(heroe))
            
        
        retorno=1
    
    return retorno
                                      
def obtener_nombre_dato(heroe:dict,key:str):
    """
    brief: devuelve el dato de un heroe en funcion a la llave que reciba en el parametro
    parameters:
    heroe:un diccionario de la lista
    key: una llave de los diccionarios
    """
    mensaje = f"nombre: {heroe['nombre']} - {key} : {heroe[key]}"
    
    '''nombres = obtener_nombre(heroe)
    #if heroe[key] != None :
    dato = f" {key} : {heroe[key]}"
    rentorno={f"{nombres} | {dato}"}  
    #else:
         #rentorno="no existe"'''             
    return  mensaje        
            
def stark_imprimir_nombres_alturas(lista:list): 
    """
    brief: imprimi los heroes con sus alturas
    parameters: 
    lista: la lista de los heroes
    """  
    retorno = -1 
    
    if len(lista) >0 :
        for heroe in lista:
            nombre=obtener_nombre(heroe)
            obtener_nombre_altura= obtener_nombre_dato(heroe,"altura")
            print(obtener_nombre_altura)
        
        retorno=1
    
    return retorno   
        
def calcular_max(lista:list,key:str):   
    """
    calcula el maximo de altura/edad/fuerza segun lo que
    reciba por parametro y devuelve el valor a donde fue llamado
    """     
    bandera_altura=True
    superheroe_mas_alto=0
    for superheroe in lista:
        
        if bandera_altura==True or float(superheroe[key]) > superheroe_mas_alto:
            bandera_altura=False
            superheroe_mas_alto= float(superheroe[key])
            nombre_del_alto = superheroe
            
    return nombre_del_alto
    
    
def calcular_min(lista:list,key:str):
    """"
    calcula el minimo de algo segun la llave y lista que le pasen por parametro
    parameters:
    lista: lista de superheroes
    key: el tipo de dato del heroe a calcular
    """
    superheroe_mas_bajo=0
    bandera_menor=True

    for superheroe in lista:
        if bandera_menor == True or float(superheroe[key]) < superheroe_mas_bajo:
            bandera_menor=False
            superheroe_mas_bajo=float(superheroe[key])
            nombre_del_bajo=superheroe
        
    return nombre_del_bajo

def calcular_max_min_dato(lista:list,tipo_calculo:str,llave:str):
    """
    brief: retorna la funcion pedida segun el tipo de calculo que pongan en el parametro 
    y su dato a informar
    parameters:
    lista:lista de los superheroes
    tipo_calculo: el tipo de dato a informar(fuerza,altura,etc)
    """
    if tipo_calculo == "maximo":
        dato_obtenido = calcular_max(lista,llave)
        
    elif tipo_calculo == "minimo":
        dato_obtenido = calcular_min(lista,llave)
    
    #print(f"el {tipo_calculo} de {llave} es {dato_obtenido} ")
    return dato_obtenido

def stark_calcular_imprimir_heroe(lista:list,tipo_calculo:str,key:str):
    """
    brief: imprime el nombre del heroe y su valor calculado
    parameters:
    lista:lista del heroe
    tipo_calculo=el dato a informar(edad,fuerza,peso etc)
    """
    info_heroe= calcular_max_min_dato(lista,tipo_calculo,key)
    datos_heroe=obtener_nombre_dato(info_heroe,key)
    imprimir_dato(datos_heroe)
    
def sumar_dato_heroe(lista:list,key:str) -> int:
    """
    brief: suma los datos de los heroes segun el dato que le pasen
    parameters:
    lista: lista de los heroes
    key: el dato a sumar 
    """
    acumulador = 0
    if len(lista) > 0 :
        for superheroe in lista:
                acumulador += float(superheroe[key])   
    else:
            print("diccionario vacio")
                
    return acumulador  

def dividir(dividendo,divisor):
    """
    dividi dos numeros
    """
    if divisor == 0 :
        retorno = 0
    else :
        retorno = dividendo/divisor
        
    return retorno

def calcular_promedio(lista:list,key:str):
    """
    calcula el promedio de un tipo de de dato de los heroes
    parameters:
    lista:lista de los heroes
    key: el tipo de dato a calcular el promedio
    """
    total_acumulador = sumar_dato_heroe(lista,key)
    total_promedio = dividir(total_acumulador,24)
    return (f"el total del promedio de {key} es: {total_promedio}")

def stark_calcular_imprimir_promedio_altura(lista:list):
    """
    imprime el promedio de altura de los superheroes
    parameters:
    lista: lista de los heroes
    """ 
    if len(lista) > 0:
        promedio_altura= calcular_promedio(lista,"altura")
        str(promedio_altura)
        imprimir_dato(promedio_altura)
        
    else:
        print("-1")

def imprimir_menu():
    menu=("""eliga una opcion:
            n1-mostrar nombre de cada heroe
            n2-Mostrar altura de cada heroe
            n3-Mostrar el heroe mas alto
            n4-Mostrar el promedio de altura de los heroes
            n5- normalizar datos de la lista
            n6-salir
            
            
            /""")
    imprimir_dato(menu)
       
def validar_entero(numero:str):
    """
    valida si el numero es un string
    parameters: 
    numero: numero a verificar
    """
    if type(numero) == str:
        retornar="true"
    else :
        retornar= "false"
    
    return retornar
    
def stark_menu_principal():
    imprimir_menu()
    respuesta=int(input("ingrese una opcion: "))
    
    
    return respuesta

def stark_marvel_app(lista_personajes):    
    while True:
        respuesta= stark_menu_principal()
        
        while respuesta <1 or respuesta >6 :
            print("ERROR REINGRESE EL NUMERO")
            respuesta=stark_menu_principal()
            
        if respuesta == 1 :
            stark_imprimir_nombres_heroes(lista_personajes)
            
        elif respuesta == 2:
            stark_imprimir_nombres_alturas(lista_personajes)
            
        elif respuesta == 3:
            valor=input("queres averiguar el minimo o maximo?:  ")
            tipo_dato=input("que queres averiguar?(altura,peso,etc) ")
            
            stark_calcular_imprimir_heroe(lista_personajes,"maximo","peso")
            stark_calcular_imprimir_heroe(lista_personajes,valor,tipo_dato)
        
        elif respuesta == 4:
            stark_calcular_imprimir_promedio_altura(lista_personajes)

        elif respuesta == 5:
           mostrar_datos_normalizados()
        elif respuesta == 6:
            break      
            
stark_marvel_app(lista_personajes)
                
                
        











