#5-
"""Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
quiera (se limita a 1 perrito por ingreso), se les pide:
nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:

1. Generar un listado con todos los datos de los pacientes ordenados por edad.
2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por
nombre.
3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
impuesto por ingresos brutos e informarlo.
4. Informar el nombre y el peso del perro con más peso."""
from os import system
system("cls")


respuesta ="si"
lista_animal=[]
lista_de_pesado=[]
acumulador_importe=0
bandera_primero=True
lista_pacientes_por_edad=[]


while respuesta == "si":
    nombre = input("nombre del animal: ")
    
    precio_consulta=int(input("ingrese el precio por la consulta(entre 500 y 2500): "))
    while precio_consulta <500 or precio_consulta >2500:
        precio_consulta=int(input("ERROR,ingrese el precio (entre 500 y 2500): "))
    
    raza=input("diga cual es la raza del perro(caniche,ovejero, siberiano): ")
    while raza !="caniche" and raza !="ovejero" and raza !="siberiano":
        raza=input("ERROR ingrese la raza que dijimos antes(caniche,ovejero, siberiano) : ")
    
    edad = int(input("ingrese la edad del animal y que este en el rango (de 1 a 15): "))
    while edad <1 or edad >15:
        edad = int(input("ingrese la edad del animal (entre 1 y 15): "))
    
    peso = float(input("ingrese el peso del perro (entre 25 y 40 kilos): "))
    while peso <25 or peso >40:
        peso = float(input("ingreseun numero que este en el rango (entre 25 y 40 kilos): "))
        
    if peso >30:
        lista_de_pesado.append(nombre)
    if bandera_primero == True:
        peso_maximo=peso
        nombre_mas_pesado=nombre
        bandera_primero=False
    elif peso >peso_maximo:
        peso_maximo=peso
        nombre_mas_pesado=nombre
        
        
    
    diccionario={"nombre":nombre,"precio x consulta":precio_consulta,"raza":raza,"edad":edad,"peso":peso} 
    lista_animal.append(diccionario)  
    
    acumulador_importe +=precio_consulta
    
    
    
    respuesta=input("queres ingresar otro animal?")
    
if acumulador_importe>5000:
    acumulador_importe=acumulador_importe*1.21
    print(f"el importe bruto con el impuesto de iva es: {acumulador_importe}")
    
print(f"el nombre del animal mas pesado es: {nombre_mas_pesado}")

lista_pacientes_por_edad=sorted(lista_animal,key=lambda x: x['edad'])


  
for animal in lista_pacientes_por_edad:    
    print(f"""el nombre es:{animal['nombre']}
            edad:{animal['edad']}
            raza:{animal['raza']}
            precio por consulta: {animal['precio x consulta']}
            peso: {animal['peso']}""")
    print("\n---------------------------------------------------------------------\n")

for i in lista_de_pesado:
    print(f"""los que pesan mas de 30 kilso son: 
            {i}""")
    print("\n----------------------------------------------------------------------\n")

#personas.sort(key=lambda x: x[1])
