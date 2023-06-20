#Realizar un programa utilizando los conceptos de la clase:
#Opciones del menú:
# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
#(terrestre, anfibio, volador).
# 2 Imprimir la lista completa de animales con su tipo.
# 3 Mostrar el porcentaje de animales por tipo.
# 4 Mayor cantidad de animales por tipo.
# 5 Menor cantidad de animales por tipo.
# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
#efectivamente está en la lista.
# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
# 8 Informar la cantidad de animales por cada tipo de animal.
# 9 Vaciar la lista.
#10 Salir.
from os import system
system("cls")


lista_animales=[]

for i in range(10):
    animal=input("ingrese un animal: ")
    
    tipo = input("ingrese de que tipo es (terrestre, anfibio, volador): ")
    
    while tipo != "terrestre" and tipo !="anfibio" and tipo !="volador":
        tipo = input("ERROR, reingrese de que tipo es (terrestre, anfibio, volador)")

    un_animal={}
    
    un_animal["animal"] = animal
    un_animal["tipo"] = tipo
    
    lista_animales.append(un_animal)
    
def imrpimir_lista_animales(lista:list):
    "recorre la lista y imprime los animales con su tipo"
    for animal in lista:
        print(f"{animal['animal']}->{animal['tipo']}")
 
def hacer_lista_tipo(lista:list): 
    """recorre la lista y hace una lista sin repetir los tipo de los animales
    parametros: recibira una lista
    devuelve la lista con los tipos sin repetir
    """
    lista_tipo_animal=[]
    
    for tipo in lista:
        lista_tipo_animal.append(tipo["tipo"])
        print(lista_tipo_animal)
        
    lista_tipo_animal = set(lista_tipo_animal)
    
    return lista_tipo_animal
 
def contador_tipo(lista:list,tipo:dict):
    """cuenta la cantidad de veces que se repiten los tipos
    como parametro va a recibir la lista y un tipo de animal
    y devuelve un contador con la cantidad de veces que se repite
    """
    contador = 0
    
    for animal in lista:
        if animal["tipo"] == tipo:
            contador +=1
            
    return contador 
        
def mostrar_porcentaje_tipo(lista:list):
    """muestra el procentaje de tipos de los animales
    y recibe una lista como parametro
    """
    
    tipos_animales=hacer_lista_tipo(lista)
    
    for tipo in tipos_animales:
        contador=contador_tipo(lista,tipo)
        porcentaje= (contador * 100) / 3
        
        print(f"de tipo animal {tipo} y el porcentaje que tiene es: {porcentaje}")
      
def mostrar_mayor_cantidad_tipo(lista:list):
    """muestra el tipo de animal que mas veces se repite
       y recibe como parametro una lista
    """
    bandera_primero = True
    contador_maximo = 0
    lista_tipos = hacer_lista_tipo(lista)
    
    for animal in lista_tipos:
        contador = contador_tipo(lista,animal)
        if bandera_primero == True or contador >contador_maximo:
            
            bandera_primero = False
            contador_maximo=contador
            tipo_animal = animal
            
    print(f" el tipo de animal que mas veces se repite es {tipo_animal} -> {contador_maximo}")        

def mostrar_menor_cantidad_tipo(lista:list):
    """muestra el tipo de animal que menos veces se repite
    y recibe como parametro una lista
    """
    bandera_primero = True
    contador_maximo = 0
    lista_tipos = hacer_lista_tipo(lista)
    
    for animal in lista_tipos:
        contador = contador_tipo(lista,animal)
        if bandera_primero == True or contador < contador_maximo:
            
            bandera_primero = False
            contador_maximo=contador
            tipo_animal = animal
            
    print(f" el tipo de animal que menos veces se repite es {tipo_animal} -> {contador_maximo}")
     
def mostrar_datos_animal(lista:list,nombre:str):
    mensaje = 0
    for animal in lista:
        
        if animal["animal"] == nombre:
            mensaje=1
            print(f"""esta en la lista:
                  {animal['animal']}-{animal['tipo']}""")
    if mensaje == 0:
        print("no esta en la lista el animal que ingresaste")
 
def mostrar_cantidad_por_tipo(lista:list):
    """muestra el procentaje de tipos de los animales
    y recibe una lista como parametro
    """
    tipos_animales=hacer_lista_tipo(lista)
    
    for tipo in tipos_animales:
        contador=contador_tipo(lista,tipo)
        
        print(f"de tipo animal {tipo} y se repiten : {contador} veces")
    

while True: 
    
    print("""ingrese una opcion: 
            # 1 Imprimir la lista completa de animales con su tipo.
            # 2 Mostrar el porcentaje de animales por tipo.
            # 3 Mayor cantidad de animales por tipo.
            # 4 Menor cantidad de animales por tipo.
            # 5 Pedir un animal e informar si está en la lista y sus datos correspondientes si
            #efectivamente está en la lista.
            # 6 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
            # 7 Informar la cantidad de animales por cada tipo de animal.
            # 8 Vaciar la lista.
            #9 Salir. """)
    opcion=int(input("ingrese una opcion: "))
    
    if opcion == 1 :
        imrpimir_lista_animales(lista_animales)
    elif opcion == 2:
        mostrar_porcentaje_tipo(lista_animales)
    elif opcion == 3:
        mostrar_mayor_cantidad_tipo(lista_animales) 
    elif opcion == 4:
        mostrar_menor_cantidad_tipo(lista_animales)
        
    elif opcion == 5:
        nombre=input("cual es el animal que queres saber?: ")
        mostrar_datos_animal(lista_animales,nombre)
        
    elif opcion == 6:
        pass
        
    elif opcion == 7:
        mostrar_cantidad_por_tipo(lista_animales)
        
    elif opcion == 8:
        lista_animales.clear()
        print(f"lista vacia {lista_animales}")
        
    elif opcion == 9:
       break
    
      
