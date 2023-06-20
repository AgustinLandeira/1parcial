
info_superheore=[
    {  
        "nombre":"super girl",
        "id": 1,
        "origen":"krypton",
        "habilidades":["volar","fuerza","velocidad","volar","fuerza","velocidad"],
        "identidad": "kara zor-El"
    },
        
    {
        "nombre":"shazam",
        "id": 25,
        "origen":"tierra",
        "habilidades":["volar","fuerza","velocidad","magia","fuerza","velocidad"],
        "identidad": "billy batson"
    
    },
    {
        
        "nombre":"power girl",
        "id": 25,
        "origen":"krypton",
        "habilidades":["volar","fuerza","congelar","congelar","congelar"],
        "identidad": "karen star"
    
    },
    
    {
        "nombre":"wonder woman",
        "id": 29,
        "origen":"amazonia",
        "habilidades":["agilidad","fuerza","lazo de la verdad","escudo",],
        "identidad": "diana prince"
    }
]    
''' 
for superheroe in info_superheore:
    id = superheroe["id"]
    nombre = superheroe["nombre"]
    origen= superheroe["origen"]
    identidad=superheroe["identidad"]
    
    print(f"""ID:{id},NOMBRE: {superheroe['nombre']}  \nidentidad: {superheroe['identidad']},origen: {superheroe['origen']}""")
    print("habilidades: ", end="")
    for habilidad in set(superheroe["habilidades"]):
        print (habilidad, end="|")
    print(" \n---------------------------------------------------------------------- \n")'''

def calcular_maximo():
    bandera_maximo=True
    maximo_altura=0
    
    for heroe in info_superheore:
        if bandera_maximo ==True and heroe["id"] > maximo_altura:
            bandera_maximo = False
            maximo_altura = heroe["id"]
            nombre = heroe["nombre"]
        elif heroe["id"] > maximo_altura:
            maximo_altura = heroe["id"]
            nombre = heroe["nombre"]
    return (f"el nombre es:{nombre} y su maximo es {maximo_altura}")

def mostrar_mayor_id ():
    
    nombre = calcular_maximo ()
    #id = calcular_maximo()
    #print(f"el nombre con mayor id es: {nombre} ")
    print(nombre)
    
def listar_hablilidades():
    lista_nueva=[]
    for superheroe in info_superheore:
        print(f"nombre:{superheroe['nombre']}")
        for habilidad in set(superheroe["habilidades"]):
            print (habilidad)
        print("\n--------------------------------------------\n")
            


def mostrar_entero(mensaje):
    numero=input(f"{mensaje} : ")
    numero=int(numero)

respuesta=True
while respuesta == True:
    opcion=int(input("ingrese un numero: "))
   # opcion=mostrar_entero("ponga una opcion para:1-mayor id-2-habilidades de cada heroe-3-salir")
    if opcion == 1:
        nombre=mostrar_mayor_id() 
        #print(nombre)    
    elif opcion == 2 :
        listar_hablilidades()
    elif opcion == 3:
        respuesta=False
        
    
    

#lista_superheroe.append(info_superheore)
#set(lista_superheroe)
#print("Habilidades: ", end="")

