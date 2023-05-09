from Data_starkkk import lista_personajes
from os import system
system("cls")

def mostrar_genero(genero:str):
    """ muestra una lista de un genero(segun cual eliga el usuario)"""
    lista_genero=[]
    for superheroe in lista_personajes:
        if superheroe["genero"] == genero:
            lista_genero.append(superheroe["nombre"])
    print(f"la lista de {genero}: {lista_genero}")
    print("\n---------------------------------------------------------------------\n")  
               
def mostrar_del_genero_mas_alto(sexo:str):
    """Recorre la lista y determinar cuál es el superhéroe más alto
    segun el género"""
    bandera_primero=True
    mas_alto=0
 
    for altura_maxima in lista_personajes:
        if bandera_primero == True and altura_maxima["genero"] == sexo:
            heroe_mas_alto = altura_maxima["nombre"]
            mas_alto = float(altura_maxima["altura"])
            bandera_primero = False
        
        elif float(altura_maxima["altura"]) > mas_alto and altura_maxima["genero"] == sexo :
            heroe_mas_alto = altura_maxima["nombre"]
            mas_alto=float(altura_maxima["altura"])
    print(f"el heroe {sexo}  mas alto es: {heroe_mas_alto} -> {mas_alto}")
    print("\n---------------------------------------------------------------------\n")
    

def mostrar_del_genero_mas_bajo(genero:str):
    """Recorre la lista y determinar cuál es el superhéroe más bajo segun el género """

    bandera_altura_minima_m=True
    peso_minimo=0

    for superheroe in lista_personajes:
        if bandera_altura_minima_m == True and superheroe["genero"]==genero:
            heroe_mas_bajo=superheroe["nombre"]
            peso_minimo=float(superheroe["altura"])
            bandera_altura_minima_m=False
        elif float(superheroe["altura"])<float(peso_minimo):
            heroe_mas_bajo=superheroe["nombre"]
            peso_minimo=float(superheroe["altura"])
    print(f"el superheroe mas bajo es: {heroe_mas_bajo} -> {peso_minimo}")

def mostrar_altura_promedio(genero:str):
    """determina la altura promedio de los superhéroes del género maculino o femenino"""
    contador=0
    acumulador_altura=0
    promedio_altura=0
    
    for heroe in lista_personajes:
        if heroe["genero"] == genero:
            contador +=1
            acumulador_altura += float(heroe["altura"])
            
    promedio_altura=acumulador_altura/contador
            
    print(f"el promedio altura de los heroes  es de un: {promedio_altura}")

def mostrar_tipo(llave:str):
    """hace una lista del tipo de un dato segun lo que reciba por parametro"""
    lista_tipo=[]
    for heroes in lista_personajes:
        
        lista_tipo.append(heroes[llave])
    
    lista_tipo=set(lista_tipo)
    
    return(lista_tipo)

def contador_de_tipos(color:str,key:str):
    """cuenta las veces que se repite un color o inteligencia depende lo que reciba
    por parametro"""
    contador=0
    
    for heroe in lista_personajes:
        if color == heroe[key]:
            contador +=1
            
                
    return contador

def mostrar_cantidades(key:str):
    """muestra las cantidades de colores que se repiten"""
    lista_de_tipos=mostrar_tipo(key)
    for tipo in lista_de_tipos:
        cantidad_segun_tipo=contador_de_tipos(tipo,key)
        print(f"la cantidad de heroes con el tipo {tipo} es de {cantidad_segun_tipo}")

def crear_lista(nombres,key):
    """pone los nombre de los heroes en un lista segun que tipo de color/inteligencia
    tenga"""
    lista=[]
    for superheroe in lista_personajes:
        if nombres == superheroe[key]:
            lista.append(superheroe["nombre"])
            
    return lista
                
def mostrar_listas_segun_tipo(llave:str):
    """muestra la lista de los superheroes por color o inteligencia"""
    nombres_segun_tipo=mostrar_tipo(llave)   
    
    for nombres in nombres_segun_tipo:
        listas_por_tipos=crear_lista(nombres,llave)
         
        print(f"los que tienen {nombres} son: ")
        print(listas_por_tipos)    

while True:
    respuesta=int(input("""
            1. mostrar nombre de cada heroe masculino
            2. Mostrar nombre de cada heroe femenino
            3. Mostrar el heroe masculino  mas alto 
            4. Mostrar  el heroe femenino  mas alto
            5. Mostrar el heroe masculino mas bajo
            6. Mostrar el heroe femenino mas bajo
            7. mostar promedio de la altura de los heroes masculinos
            8. mostar promedio de la altura de los heroes femeninos
            9. mostrar cantidad de colores de ojos
            10.mostrar cantidad de colores de pelo
            11. mostrar la cantidad de inteligencia de cada heroe
            12. mostrar listas de heroes segun su color de ojos
            13. mostrar una lista de superheroes separados por color de pelo
            14. mostrar un lista por heroe segun su inteligencia
            15. salir
            ELIJA UNA OPCION: """))
        
    if respuesta == 1 :
        mostrar_genero("M")
    elif respuesta == 2:
        mostrar_genero("F")
    elif respuesta == 3:
        mostrar_del_genero_mas_alto("M")
        
    elif respuesta == 4:
        mostrar_del_genero_mas_alto("F")
        
    elif respuesta == 5:
        mostrar_del_genero_mas_bajo("M")
        
    elif respuesta == 6:
        mostrar_del_genero_mas_bajo("F")
        
    elif respuesta == 7:
        mostrar_altura_promedio("M")
        
    elif respuesta == 8:
        mostrar_altura_promedio("F")
        
    elif respuesta == 9:
        mostrar_cantidades("color_ojos")
        
    elif respuesta == 10:
        mostrar_cantidades("color_pelo")
        
    elif respuesta== 11 :
        mostrar_cantidades("inteligencia")
        
    elif respuesta == 12 : 
        mostrar_listas_segun_tipo("color_ojos")
        
    elif respuesta == 13 :
        mostrar_listas_segun_tipo("color_pelo")
        
    elif respuesta == 14:
        mostrar_listas_segun_tipo("inteligencia")
        
    elif respuesta == 15:
        break
    
    

            
            
    

        
