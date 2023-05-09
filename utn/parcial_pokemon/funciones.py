from ejercicio_pokemon import *
from archivo_csv import traer_csv

def imprimir_menu():
    print("""
            1. traer datos desde  archivo
            2. mostrar la cantidad de tipos de pokemones
            3. mostrar nombre y poder de los pokemones por tipo
            4. buscar pokemon segun la descripcion de la habilidad 
            5. Mostrar pokemones en orden segun su poder de ataque
            6. generar un archivo json con un tipo de los pokemones
            7. leer el json que creaste
            8. agregar un pokemon a la lista
            9 . salir del menu""")

def pokemon_menu_principal()->int:
    imprimir_menu()
    
    respuesta = (input("ingrese un numero segun la opcion que quieras : "))
    
        
    while re.match("[a-zA-Z]",respuesta):
        respuesta = (input("ingrese un numero segun la opcion que quieras : "))
    
        
    respuesta = int(respuesta)   
    
    return respuesta

def pokemon_app_():
    
    lista_creada = False
    while True:
        
        if lista_creada == False:
            
            print("***************************************************************************\n")
            print("ACLARACION: TENES QUE TRAER EL CSV DE LA OPCION UNO PARA PODER ELEGIR MAS OPCIONES\n")
            print("**********************************************************************************\n")
            
        respuesta = pokemon_menu_principal()
        
        if respuesta <10 and type(respuesta) == int:
        
            if respuesta == 1:
                lista_creada = True
                lista_pokemones=traer_csv("pokemones.csv")
                
                
            elif respuesta == 2 and lista_creada == True:
                
                mostrar_lista_tipos(lista_pokemon)
            
            elif respuesta == 3 and  lista_creada == True :
                
                listar_pokemones_por_tipo(lista_pokemon)
                
            elif respuesta == 4 and lista_creada == True:
                habilidad = input("ingrese la habilidad que queres: ")
                
                listar_pokemon_habilidad(habilidad,lista_pokemon)
                
            elif respuesta == 5 and lista_creada == True :
                listar_pokemones_orden(lista_pokemon,"ataque")
                
            elif respuesta == 6 and lista_creada == True :
                archivo = input("crea un nombre para un archivo json: ")
                tipo= input("que tipo de pokemon buscas?: ")
                guardar_json(archivo,tipo,lista_pokemon)
                
            elif respuesta == 7 and lista_creada == True :
                path = input("ingrese el nombre del archivo que se creo para leerlo: ")
                leer_json(path)
                
            elif respuesta ==8 and lista_creada == True:
                lista_pokemon = agregar_pokemon(lista_pokemon)
            
            elif respuesta == 9:
                print("acabas de cerrar la aplicacion")
                
                break
        else:
            respuesta=int(input("error reingrese el numero"))
            
        if lista_creada == True:
            
            lista_pokemon = lista_pokemones
        
        
            
pokemon_app_()
