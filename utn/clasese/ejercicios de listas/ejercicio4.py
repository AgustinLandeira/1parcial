"""Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto
El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
(validar). El valor por defecto para los senadores ausentes será Abstención.
Se deberá Informar:

o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla."""

from os import system
system("cls")

respuesta="si"
contador_senadores=0
senadores_presentes=0
contador_afirmativo=0
contador_negativo=0
contador_abstencion=0

lista_afirmativos=[]
lista_negativos=[]
lista_abstencion=[]

while respuesta == "si":
    
    nombre=input("ingrese el nombre del senador: ")
    presencia=input("esta presente?: ")
    
    if presencia =="si":
        valor_voto=input("ingrese su valor al voto(afirmativo,negativo o abstencion): ")
        senadores_presentes +=1
        while valor_voto !="afirmativo" and valor_voto !="negativo" and valor_voto !="abstencion":
            valor_voto=input("ERROR,ingrese su valor al voto(afirmativo,negativo o abstencion): ")
    else:
        valor_voto="abstencion" 
        
    if valor_voto =="afirmativo":
        contador_afirmativo +=1
        lista_afirmativos.append(nombre)
        
    elif valor_voto =="negativo":
        contador_negativo +=1
        lista_negativos.append(nombre)
    else:
        contador_abstencion +=1
        lista_abstencion.append(nombre)   
    
    
    
    contador_senadores += 1   
    respuesta=input("queres ingresar otro voto?: ")
    
porcentaje_afirmativo = (contador_afirmativo*100)/senadores_presentes
porcentaje_negativo = (contador_negativo*100)/senadores_presentes
porcentaje_abstencion= (contador_abstencion*100)/senadores_presentes

for afirmativo in lista_afirmativos:
    print(f"""los votos afirmativos fueron: 
            {afirmativo}""")
print("\n-------------------------------------------------------------------\n")
for negativo in lista_negativos:
    print(f"los votos negativos fueron: {negativo}")
print("\n-------------------------------------------------------------------\n")
for abstencion in lista_abstencion:
    print(f"los votos de abstencion fueron: {abstencion}")
print("\n-------------------------------------------------------------------\n")
    
       
print(f"la cantidad de senadores que hay en total son: {contador_senadores} senadores")  
print(f"la cantidad de senadores presente son: {senadores_presentes} presentes") 
print(f"""la cantidad de votos afirmativos son: {contador_afirmativo} 
    y el porcentaje que saco fue de un : {porcentaje_afirmativo}%""")
print(f"el porcentaje de votos negativos es de un {porcentaje_negativo}")
print(f"el porcentaje de votos de abstencion es de un {porcentaje_abstencion}% ")
print("\n--------------------------------------------------------------\n")


    