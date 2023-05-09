import re
from os import system
system("cls")

def imprimir_dato(dato:str):
    """
    brief :muestra un mensaje solo si es una  cadena
    parameters: un dato en cadena 

    """
    if type(dato) == str :
        print(dato)

def imprimir_menu_desafio_5():
    print("""
            a. mostrar nombre de cada heroe masculino
            b. Mostrar nombre de cada heroe femenino
            c. Mostrar el heroe masculino  mas alto 
            d. Mostrar  el heroe femenino  mas alto
            e. Mostrar el heroe masculino mas bajo
            f. Mostrar el heroe femenino mas bajo
            g. mostar promedio de la altura de los heroes masculinos
            h. mostar promedio de la altura de los heroes femeninos
            i. mostrar cantidad de colores de ojos
            j.mostrar cantidad de colores de pelo
            k. mostrar la cantidad de inteligencia de cada heroe
            l. mostrar listas de heroes segun su color de ojos
            m. mostrar una lista de superheroes separados por color de pelo
            n. mostrar un lista por heroe segun su inteligencia
            z. salir""")
    #imprimir_dato()
    
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    
    respuesta = input("ingrese una letra que este en el menu: ")
    
    if re.match("[a-nA-N]",respuesta) and len(respuesta) <2:
        retornar = respuesta
        
    else:
        retornar = -1
    
    return retornar

'''def stark_marvel_app_5(lista_heroes:list):
    
    respuesta = stark_menu_principal_desafio_5()
    
    if respuesta == "a" :
        #mostrar_genero("M")
    elif respuesta == "b":
        mostrar_genero("F")
    elif respuesta == "c":
        mostrar_del_genero_mas_alto("M")
        
    elif respuesta == "d":
        mostrar_del_genero_mas_alto("F")
        
    elif respuesta == "e":
        mostrar_del_genero_mas_bajo("M")
        
    elif respuesta == "f":
        mostrar_del_genero_mas_bajo("F")
        
    elif respuesta == "g":
        mostrar_altura_promedio("M")
        
    elif respuesta == "h":
        mostrar_altura_promedio("F")
        
    elif respuesta == "i":
        mostrar_cantidades("color_ojos")
        
    elif respuesta == "j":
        mostrar_cantidades("color_pelo")
        
    elif respuesta== "k" :
        mostrar_cantidades("inteligencia")
        
    elif respuesta == "l" : 
        mostrar_listas_segun_tipo("color_ojos")
        
    elif respuesta == "m" :
        mostrar_listas_segun_tipo("color_pelo")
        
    elif respuesta == "n":
        mostrar_listas_segun_tipo("inteligencia")
        
    elif respuesta == "0":
        break
    '''

def leer_archivo(nombre_archivo:str,extension:str):
    if type(nombre_archivo) == str and type(extension) == str:
        if extension == ".json":
            import json
            with open(nombre_archivo,"r") as archivo:
                lista = archivo.read()
                
                return lista
        elif extension == ".csv":
            lista=[]
            with open(nombre_archivo,"r") as archivo:
                for line in archivo:
                    registro={}
                    datos=re.split(",|\n",line)
                    registro["nombre"] = datos[0]
                    registro["identidad"] = datos[1]
                    registro["empresa"] = datos[2]
                    registro["altura"] = datos[3]
                    registro["peso"] = datos[4]
                    registro["genero"] = datos[5]
                    registro["color_ojos"] = datos[6]
                    registro["color_pelo"] = datos[7]
                    registro["fuerza"]=datos[8]
                    registro["inteligencia"]=datos[9]
                    
                    lista.append(registro)
                    
            return lista
       
lista_heroes=leer_archivo("data_stark.csv",".csv") 

for heroe in lista_heroes:
    print(f"el nombre es: {heroe['nombre']}")
    
    #print(heroe['nombre'])   









