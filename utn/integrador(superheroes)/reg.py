
import re 
from Data_stark import lista_personajes
from os import system
system("cls")

def extraer_iniciales(nombre_heroe:str):
    mensaje =  ""
    
    nombre_heroe = re.sub("-"," ",nombre_heroe)
    palabras = re.split(" ",nombre_heroe)
    
    if nombre_heroe != " ":
        for palabra in palabras:
            if (re.search("the",palabra)) != None:
                pass
            else:
                inicial = palabra[0]
                mensaje += inicial + "."
    else:
        mensaje = "N/A"            
            
    return mensaje
            
    
    
def definir_iniciales_nombre(heroe:dict):
    retorno=True
    
    if type(heroe) == dict:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        
        if heroe["iniciales"] == "N/A":
            retorno = False
            
    return retorno
        
def agregar_iniciales_nombre(lista_heroes:list):
    
    if type(lista_heroes) == list and len(lista_heroes) >0:
        
        for heroe in lista_heroes:
            retorno = definir_iniciales_nombre(heroe)
            
            if retorno == False:
                print("los datos no contienes un buen formato")
                break
            else:
                retorno = True
    
    return retorno
        

def stark_imprimir_iniciales(lista_heroes:list):
    
    iniciales = agregar_iniciales_nombre(lista_heroes)
    
    if iniciales == True:
        
        for heroe in lista_heroes:
            print(f"*{heroe['nombre']}({heroe['iniciales']})")

def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip()
    
    if re.search("[a-z]",numero_str) != None:
        retornar = -1
        
    elif re.search("^-",numero_str):
        retornar = -2
        
    elif re.search("[0-9]",numero_str):
        retornar=int(numero_str)
    else:
        retornar = -3
    
    print(retornar)
    
sanitizar_entero("123-")


