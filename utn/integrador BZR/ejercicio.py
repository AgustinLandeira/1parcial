from Data import lista_bzrp
from funciones import *
from os import system
system("cls")


def calcular_maximo(lista:list,clave:str)->int:
    maximo=0
    bandera_prime_tema=False
    
    if(type(lista) == list) and type(clave) == str and len(lista >0):
    
        for cancion in lista:
            if cancion[clave]> maximo or bandera_prime_tema ==False:
                bandera_prime_tema=True
                maximo=cancion[clave]
    return maximo

def mostrar_temas_con_mas_reproducciones (lista:list) :
    
    maximo_reproducciones=calcular_maximo(lista,"views")
    
    print("temas con mayor cantidad de reproducciones:")
    mostrar_algunos_temas(lista,"views",maximo_reproducciones)
    


def mostar_temas_menos_vistos():
    minimo_reproducciones =0
    bandera_primer_tema= False
    
    for cancion in lista_bzrp:
        if cancion["views"] < minimo_reproducciones or bandera_primer_tema == False:
            bandera_primer_tema=True
            minimo_reproducciones = cancion["views"]
    
    print("temas con menor cantidad de reproducciones")
    for cancion in lista_bzrp:
        if cancion["views"] == minimo_reproducciones:
            mostrar_video(cancion)


def mostrar_tema_mas_largo(lista:list):
    maximo_largo=calcular_maximo(lista,"length")
    
    print("temas con mayor duracion:")
    mostrar_algunos_temas(lista,"leght",maximo_largo)


respuesta=True

while respuesta ==True:
    
    respuesta=int(input("""
                    opcion1: mostrar temas 
                    opcion 2: mostrar temas mas vistos 
                    opcion 3: mostrar temas menos vistos
                    opcion 4 mostrar suma de reproducciones
                    opcion 5 mostrar promedio de reproducciones
                    opcion 6 mostrar tema mas largo
                    eliga una opcion: """))
    
    if respuesta == 1:
        mostrar_temas(lista_bzrp)
    elif respuesta== 2:
        mostrar_temas_con_mas_reproducciones(lista_bzrp)
        pass
    elif respuesta ==3:
        pass
    elif respuesta == 4:
        pass
    elif respuesta == 5:
        pass
    elif respuesta == 6:
        mostrar_tema_mas_largo(lista_bzrp)
    elif respuesta == 7:
        break
                    


