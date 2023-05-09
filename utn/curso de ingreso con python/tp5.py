#Bienvenidos.
#Realizar el algoritmo que permita ingresar el nombre de un animal del zoológico,
# el peso el cual debe ser entre 1 y 1000 y
#la temperatura del hábitat (entre -30 y 30) hasta que el usuario quiera 
# e informar al terminar el ingreso por document.write:
#a) La cantidad de temperaturas pares.
#b) El nombre y temperatura del animal más pesado
#c) La cantidad de animales que viven a menos de 0 grados.
#d) El promedio del peso de todos los animales.
#f) El peso máximo y el mínimo de todos los animales cuyas temperaturas sean bajo cero.

seguir="si"
contador_par=0
bandera_primero=True
contador_animal_menos_cero=0
contador_animal=0
acumulador_de_peso=0

while seguir=="si":
    nombre_del_animal=input(" ingrese el nombre del animal: ")
    peso_ingresado=float(input("ingrese el peso del animal: "))
    while(peso_ingresado<1 or peso_ingresado>1000):
        peso_ingresado=int(input("ERROR ingrese el peso del animal entre 1 y 1000 : "))
    
    temperatura_del_habitat=float(input("ingrese la temperatura del habitat: "))
    while temperatura_del_habitat<-30 or temperatura_del_habitat>1000:
        temperatura_del_habitat=float(input("ingrese la temperatura del habitat(entre -30 y 30) "))
    
    if temperatura_del_habitat %2==0:
        contador_par=contador_par+1

    if bandera_primero==True:
        nombre_del_mas_pesado=nombre_del_animal
        mas_pesado=peso_ingresado
        tem_del_mas_pesado=temperatura_del_habitat
        bandera_primero=False
    else:
        if peso_ingresado>mas_pesado:
            nombre_del_mas_pesado=nombre_del_animal
            mas_pesado=peso_ingresado
            tem_del_mas_pesado=temperatura_del_habitat
            
            
    if temperatura_del_habitat <0:
        contador_animal_menos_cero=contador_animal_menos_cero+1
        
    contador_animal=contador_animal+1
    acumulador_de_peso+=peso_ingresado
    
    seguir=input("desea ingresar otro animal?: ")
   
   

promedio=acumulador_de_peso/contador_animal
print(f"la cantidad de numeros pares en total es: {contador_par}")
print(f"el nombre del animal mas pesado se llama: {nombre_del_mas_pesado} y su temp es {tem_del_mas_pesado}")
print(f"la cantidad de animales que viven con menos de 0 grado en total es: {contador_animal_menos_cero}")
print(f"el promedio de peso de los animales ingresados es: {promedio}")
