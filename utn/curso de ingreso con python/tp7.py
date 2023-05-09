
#3) Copa pistón!!!
#Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
#Se pedirá el ingreso de:
#nombre
# edad (mayor a 18)
#nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
 #cantidad de carreras ganadas (no pueden ser números negativos)
 #número del vehículo (no puede ser un número negativo)
#se necesita saber:
#Nacionalidad del piloto más joven.
#Cantidad de vehículos con número par.
#Nombre del piloto con menos victorias y el número de auto impar.
#Cantidad de pilotos mayores de 25 años con número de vehículo impar.
#Nombre del piloto más joven con más victorias.
#Nacionalidad del piloto más veterano con menos victorias.
#Promedio de edad de los pilotos que tiene un vehículo con número par.
#/

bandera_primero=True
contador_par=0
bandera_segundo=True
contador_pilotos=0
acumulador_de_edad=0
contador_de_edad=0



for i in range(3):
    nombre=input("ingrese nombre del piloto: ")
    
    edad_ingresada=int(input("ingrese la edad (mayor a 18): "))
    while edad_ingresada<18:
        edad_ingresada=int(input("ERROR,ingrese la edad (mayor a 18): "))
        
    nacionalidad=input("""ingrese la nacionalidad 
                (argentino, inglés, francés, brasilero, estadounidense): """)
    while (nacionalidad !="argentino" and nacionalidad !="ingles" and nacionalidad !="frances"
           and nacionalidad!="brasilero" and nacionalidad !="estadounidense"):
        nacionalidad=input("ERROR nacionalidad incorrecta,ponga el dato devuelta: ")   
         
    carreras_ganadas=int(input("cuantas carreras gano: "))
    while carreras_ganadas<0:
        carreras_ganadas=int(input(" reingrese cuantas carreras gano: "))
        
    numero_del_vehiculo=int(input("ponga el numero del auto: "))
    while numero_del_vehiculo <0:
        numero_del_vehiculo=int(input("el numero no puede ser negativo: "))
    
    if bandera_primero==True:
        edad_minima=edad_ingresada
        nacionalidad_mas_joven=nacionalidad
        bandera_primero=False
        nombre_mas_joven=nombre
        victorias_del_mas_joven=carreras_ganadas
        
    elif edad_ingresada<edad_minima:
        edad_minima=edad_ingresada
        nacionalidad_mas_joven=nacionalidad 
        nombre_mas_joven=nombre
        victorias_del_mas_joven=carreras_ganadas  

    if numero_del_vehiculo %2 ==0:
        contador_par=contador_par+1
        acumulador_de_edad+=edad_ingresada   
        contador_de_edad=contador_de_edad+1
        
    elif bandera_segundo==True:
        numero_impar=numero_del_vehiculo
        nombre_menos_victorias=nombre
        victorias_minimas=carreras_ganadas
        bandera_segundo=False
       
        
    elif carreras_ganadas<victorias_minimas:
        numero_impar=numero_del_vehiculo
        nombre_menos_victorias=nombre
        victorias_minimas=carreras_ganadas
        
    if edad_ingresada >25 and numero_del_vehiculo %2 !=0:
        contador_pilotos=contador_pilotos+1
        
   

promedio=acumulador_de_edad/contador_de_edad


print(f"la nacionalidad del piloto mas joven es: {nacionalidad_mas_joven}")
print(f"las cantidad de numeros pares delos  vehiculos son: {contador_par}")
print(f"""el nombre del piloto con menos victorias es: {nombre_menos_victorias} y su numero
      impar es : {numero_impar}""")
print(f"la cantidad de pilotos mayores de 25 años con numero impar es: {contador_pilotos}")
print(f" la cantidad de victorias del chico mas joven es:  {victorias_del_mas_joven}")
print(f"el promedio de edad es: {promedio}")

