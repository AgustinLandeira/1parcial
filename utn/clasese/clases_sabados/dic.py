from os import system
system("cls")
'''1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego
imprimir por pantalla el nombre y la edad de cada persona.'''

'''lista = []
for i in range (5):
    
    
    nombre = input("ingrese su nombre: ")
    edad = input("ingrese su edad: ")
    
    una_persona={}
    una_persona["nombre"] = nombre
    una_persona["edad"] = edad
    
    lista.append(una_persona)
 
print(lista)   
for persona in lista:
    print(f"{persona['nombre']}-{persona['edad']}")'''

###################################################################################

'''2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10
paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por
pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.'''

'''lista_paises=[
    {
        "pais":"argentina",
        "capital": "buenos aires"
    },
    {
        "pais":"brasil",
        "capital": "brasilia"
    },
    {
        "pais": "peru",
        "capital": "lima"
    },
    {
        "pais":"colombia",
        "capital": "bogota"
    },
    {
        "pais":"chile",
        "capital": "santiago"
    },
    {
        "pais":"uruguay",
        "capital": "montevideo"
    },
    {
        "pais":"bolivia",
        "capital": "quito"
    }
    
]

while True :
    mensaje = ""
    pais = input("ingrese el pais asi le decimos la capital(que este en la lista) o s para salir: ")
    
    if pais == "s":
        break
    else:
        for nombre in lista_paises:
            if nombre["pais"] == pais:
                mensaje = (f"el pais que eligio es {nombre['pais']} y su capital es {nombre['capital']}")
    if mensaje == "":
        mensaje=("el pais no esta en la lista")
                 
    print(mensaje)
    

'''
##################################################################################
#3. Crear un diccionario que contenga los nombres de 10 frutas y su precio en dolares.
#Pedir al usuario que ingrese el nombre de una fruta y luego imprimir en pantalla su
#precio correspondiente en pesos.
'''lista_fruta=[]
for i in range(3):
    fruta = input("ingrese la fruta: ")
    precio = int(input(" ingrese su precio en dolares: "))
    
    una_fruta={}
    una_fruta["fruta"] = fruta
    una_fruta["precio"] = precio
    lista_fruta.append(una_fruta)
    
fruta_elegida=input("dime la fruta que quieras saber: ")

for opcion in lista_fruta:
    if opcion["fruta"] == fruta_elegida:
        total_en_pesos = 500* int(opcion["precio"]) 
        print(f" el precio en pesos es: {total_en_pesos}")
'''
#######################################################################################

'''4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas
que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la
cantidad de patas correspondiente.'''

'''animales = {
    "perro": 4,
    "gato": 4,
    "araña": 8,
    "pollo": 2,
    "serpiente": 0
}

animal = input("ingrese el animal: ")

'''
###############################################################################################
'''7. Crear un diccionario que contenga los nombres, edades, alturas (en metros), pesos (en
kilogramos) y ciudades de un numero indeterminados de personas. Luego calcular el
indice de masa corporal (IMC) de cada persona y agregarlo al diccionario. Finalmente,
imprimir en pantalla los nombres de las personas junto con su ciudad y si IMC
(redondeando a 2 decimales).
'''
'''respuesta = "si"
lista_personas = []
while respuesta == "si":
    nombre = input("ingrese su nombre: ")
    edad = input("ingrese su edad: ")
    altura = float(input("ingrese su altura: "))
    peso = int(input("ingrese su peso: "))
    ciudad = input("ingrese su ciudad: ")
    
    una_persona={}
    una_persona["nombre"]=nombre
    una_persona["edad"]=edad
    una_persona["altura"]=altura
    una_persona["peso"]=peso
    una_persona["ciudad"]=ciudad
    
    lista_personas.append(una_persona)
    
    respuesta = input("queres ingresar mas datos?: ")
    
for persona in lista_personas:
    persona["imc"] = persona["peso"]/(persona["altura"] ** 2)
    persona["imc"] = round(persona["imc"],2)
    
    print(f"nombre: {persona['nombre']}-ciudad:{persona['ciudad']}-imc: {persona['imc']}")
    '''
######################################################################################################################
#8. Crear un diccionario que contenga los nombres, edades, salario por día, días trabajados
#de 10 empleados. Luego, calcular el salario total de cada empleado y agregarlo al
#diccionario. Finalmente, imprimir en consola los nombres de los empleados junto con
#la edad y el salario total.

'''lista_empleados = []

for i in range(2):
    nombre = input("ingrese el nombre del empleado: ")
    edad = int(input("ingrese la edad del empleado: "))
    salario_dia = float(input("ingrese el salario por dia del empleado: "))
    dias_trabajados = int(input("ingrese los dias trabajados del empleado: "))
    
    un_empleado = {}
    un_empleado["nombre"] = nombre
    un_empleado["edad"] = edad
    un_empleado["por dia"] = salario_dia
    un_empleado["dias trabajados"] = dias_trabajados
    
    lista_empleados.append(un_empleado)

for empleado in lista_empleados:

    salario_en_total = empleado["por dia"] * empleado["dias trabajados"]
    empleado["salario"] = salario_en_total
    
    print(f"""
              NOMBRE: {empleado['nombre']}
              EDAD : {empleado['edad']}
              SALARIO: {empleado['salario']}""")
    
print(lista_empleados)        
    
'''
#########################################################################################################
#9. Crear un diccionario que contenga los nombres, edades, fechas de nacimiento, numeros
#de telefono y correos electrónicos de un numero indeterminado de personas. Luego,
#concatenar la fecha de nacimiento y el número de teléfono de cada persona con el
#formato “11-1111-1111 – dd/mm/aaaa” y agregarlo al diccionario (usar un string
#interpolado con format para hacerlo más facil). Finalmente imprimir en consola el
#nombre, correo electrónico y los datos concatenados.
#lista = []
import re

'''while True:
    
    nombre= input("ingrese el nombre: ")
    edad= input("ingrese la edad: ")
    fecha_nacimiento= input("ingrese la fecha de nacimiento: ")
    numero_de_telefono= input("ingrese el numero de telefono: ")
    correo= input("ingrese el correo electronico: ")
    
    una_persona = {}
    una_persona["nombre"] = nombre
    una_persona["edad"] = edad
    una_persona["nacimiento"] = fecha_nacimiento
    una_persona["telefono"] = numero_de_telefono
    una_persona["correo"] = correo
    
    lista.append(una_persona)
    
    respuesta=input("queres ingresar mas datos?: ")
    
    if respuesta == "no":
        break
for persona in lista:
    fecha =   re.sub("de"," ",persona["nacimiento"]) 
    formato = fecha.split(" ")
    formato = formato.split(" ")
    print(formato)
    dia = formato[0]
    mes= formato[1]
    print(dia,mes)
    #print(f"{formato[0]}/{formato[1]}/{formato[2]}")
    '''
#############################################################################################################
#12. Crear una lista de diccionarios que contenga información sobre 5 libros, incluyendo
#título, autor, editorial, año de publicación, y género. Luego, pedir al usuario que ingrese un
#género y mostrar en pantalla todos los títulos de ese género con todos los datos.
'''lista_libros=[]

for i in range (5):
    titulo=input("ingrese el titulo del libro:  ")
    autor=input("ingrese el autor del libro:  ")
    editorial=input("ingrese la editorial del libro:  ")
    año_publicacion=int(input("ingrese el año de la publicacion del libro:  "))
    genero=input("ingrese el genero del libro:  ")
    
    un_libro = {}
    un_libro["titulo"] = titulo
    un_libro["autor"] = autor
    un_libro["editorial"] = editorial
    un_libro["publicacion"] = año_publicacion
    un_libro["genero"] = genero
    
    lista_libros.append(un_libro)
tipo=input("ingrese el genero para ver que libros hay disponibles: ")
 
for libro in lista_libros:
    if tipo == libro["genero"]:
        print(f"""
              {libro['titulo']}
              {libro['autor']}
              {libro['editorial']}
              {libro['publicacion']}
              {libro['genero']}""")'''
##########################################################################################################
#13. Crear una lista de diccionarios que contenga información sobre 5 películas, incluyendo
#título, director, año de estreno, género y duración en minutos. Luego, pedir al usuario
#que ingrese una duración máxima y mostrar por consola los títulos de las películas que
#no excedan esa duración ordenado alfabéticamente por nombre de la pelicula (pueden
#usar listas auxiliares para guardar datos).
'''lista = []
for i in range(3):
    
    titulo = input("titulo de la pelicula: ")
    director = input("ingrese el director: ")
    estreno = int(input("ingrese el año de estreno: "))
    genero = input("ingrese el genero: ")
    duracion = int(input("ingrese los minutos que dura la pelicula: "))
    
    una_pelicula={}
    una_pelicula["titulo"] = titulo
    una_pelicula["director"] = director
    una_pelicula["estreno"] = estreno
    una_pelicula["genero"] = genero
    una_pelicula["duracion"] = duracion
    
    lista.append(una_pelicula)
    
duracion_maxima = int(input("ingrese la duracion maxima: "))
lista_nombre=[]
for pelicula in lista:
    
    if pelicula["duracion"] < duracion_maxima:
        lista_nombre.append(pelicula["titulo"])
        
lista_ordenada = sorted(lista_nombre)  
print(lista_ordenada)     '''
 #######################################################################################
'''
14. Crear una lista de diccionarios que contenga la información de 10 canciones incluyendo
nombre del artista, titulo de la cancion, álbum al que pertenece, año de lanzamiento y
duración en segundos. Luego, pedir al usuario que ingrese una duración mínima y
mostrar por consola de forma diferenciada las canciones que tengan menor tiempo y
mayor tiempo con respecto al ingresado por el usuario.
'''

'''
lista = []
lista_menor_duracion = []
lista_mayor_duracion = []
for i in range(3):
    
    artista = input("nombre del artista: ")
    titulo = input("ingrese el titulo de la cancion: ")
    albun = input("ingrese el albun que pertenece: ")
    año_lanzamiento = int(input("ingrese el año de lanzamiento : "))
    duracion = int(input("ingrese los segundos que dura la cancion: "))
    
    una_cancion={}
    una_cancion["artista"] = artista
    una_cancion["titulo"] = titulo
    una_cancion["albun"] = albun
    una_cancion["lanzamiento"] = año_lanzamiento
    una_cancion["duracion"] = duracion
    
    lista.append(una_cancion)
    
duracion_minima = int(input("ingrese una duracion minima"))

for cancion in lista:
    if cancion["duracion"] < duracion_minima:
        lista_menor_duracion.append(cancion)
    else:
        lista_mayor_duracion.append(cancion)
    
print(f"los que tiene menos duracion es: {lista_menor_duracion}\n") 
print(f"los que tiene menos duracion es: {lista_mayor_duracion}\n") 
'''  
#########################################################################################################
'''15. Crear una aplicación que permita a los usuarios agregar y buscar películas de una lista
de diccionarios. Cada diccionario debe contener información sobre una película,
incluyendo su titulo, director, año de estreno, genero, y duración en minutos. Al iniciar
la aplicación, se debe mostrar un menú que permita al usuario elegir entre agregar una
película o buscar una película por título. Si el usuario elige agregar una película, se
deben pedir los datos por consola y agregarlos a la lista de diccionarios. Si el usuario
elige buscar una película por título, se le debe pedir el nombre de la película que busco
por consola y mostrar en pantalla la información completa de la película si existe o un
mensaje indicando que la película no se encuentra en el listado.
'''
lista_peliculas = []
def agregar_pelicula(lista:list):
    titulo = input("titulo de la pelicula: ")
    director = input("ingrese el director: ")
    estreno = int(input("ingrese el año de estreno: "))
    genero = input("ingrese el genero: ")
    duracion = int(input("ingrese los minutos que dura la pelicula: "))
    
    una_pelicula={}
    una_pelicula["titulo"] = titulo
    una_pelicula["director"] = director
    una_pelicula["estreno"] = estreno
    una_pelicula["genero"] = genero
    una_pelicula["duracion"] = duracion
    
    lista.append(una_pelicula)
    
    return lista

def buscar_lista(titulo:str):
    
    for pelicula in lista_peliculas:
        if pelicula["titulo"] == titulo:
            print(f"""
                  NOMBRE:{pelicula['titulo']}
                  DIRECTOR:{pelicula['director']}
                  ESTRENO:{pelicula['estreno']}
                  GENERO:{pelicula['genero']}
                  DURACION:{pelicula['duracion']}""")
        else:
            print("la pelicula no esta en la lista")    
  

while True:
    print("""
           opcion 1 : para buscar una peli
           opcion 2: agregar una peli
           opcion 3 : salir""")
    respuesta = int(input("ingrese su opcion: "))
    
    if respuesta == 1:
        titulo = input("ingrese el titulo de la pelicula")
        buscar_lista(titulo)
        
    elif respuesta == 2:
        
        agregar_pelicula(lista_peliculas)
        
    elif respuesta == 3:
        break











