""""Al presionar el botón pedir números hasta que el usuario quiera, mostrar:
1-Suma de los negativos. 
2-Suma de los positivos. 
3-Cantidad de positivos. 
4-Cantidad de negativos. 
5-Cantidad de ceros. 
6-Cantidad de números pares. 
7-Promedio de positivos. 
8-Promedios de negativos. 9-Diferencia entre positivos y negativos, (positvos-negativos)."""

seguir="si"
suma_de_positivos=0
suma_de_negativos=0
contador_positivos=0
contador_negativos=0
contador_ceros=0
contador_de_numeros_pares=0


while seguir=="si":
    numero_ingresado= int(input("ingrese un numero: "))
    
    if numero_ingresado>0:
       suma_de_positivos+=numero_ingresado
       contador_positivos=contador_positivos+1
    else: 
        suma_de_negativos+=numero_ingresado
        contador_negativos=contador_negativos+1
    if numero_ingresado==0:
        contador_ceros=contador_ceros+1
        
    if numero_ingresado %2 ==0:
        contador_de_numeros_pares=contador_de_numeros_pares+1
    seguir=input("queres ingresar otro numero?: ")
    
    
if contador_positivos== 0:
    suma_de_positivos="no ha positivos"
    contador_positivos="no hay positivos para contar"
    promedio_positivo="no se puede hacer este promedio"
else:
    promedio_positivo= suma_de_positivos/contador_positivos

if contador_negativos==0:
    suma_de_negativos="no hay numeros negativos"
    contador_negativos="no hay numeros negativos para contar"
    promedio_negativos= "no se puede hacer el promedio"
else:    
    promedio_negativos=suma_de_negativos/contador_negativos
    
if contador_negativos==0 or contador_positivos==0:
    diferencia="faltan numeros para hacer esta cuenta"
#else:
    #diferencia=str(suma_de_positivos - suma_de_negativos)


if contador_negativos==0:
    suma_de_negativos="no hay numeros negativos"
    contador_negativos="no hay numeros negativos para contar"
    promedio_negativos="no se puede hacer el promedio"
if contador_ceros ==0:
    contador_ceros="no ingresaste ceros"
elif contador_de_numeros_pares==0:
    contador_de_numeros_pares="no hay numero pares"

print(f"la suma de los numeros positivos en total es: {suma_de_positivos} y la cantidad es: {contador_positivos}")
print(f"la suma de los numeros negativos {suma_de_negativos} y la cantidad es: {contador_negativos}")
print(f"la cantidad de ceros es: {contador_ceros}")
print(f"la cantidad de numeros pares que hay en total son: {contador_de_numeros_pares} numeros")
print(f"el promedio de positivos es de un : {promedio_positivo} y de los negativos {promedio_negativos}")

