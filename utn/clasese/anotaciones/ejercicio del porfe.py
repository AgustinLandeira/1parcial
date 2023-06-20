from Data import lista_bzrp
from os import system

def mostrar_temas():
    print("Lista de temas: ")
    for cancion in lista_bzrp:
        print(cancion["title"])

def mostrar_el_maximo():
    maximos_reproducciones = 0
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["views"] > maximos_reproducciones or bandera_primer_tema == False:
            bandera_primer_tema = True
            maximos_reproducciones = cancion["views"]
    for cancion in lista_bzrp:
        if cancion["views"] == maximos_reproducciones:
            print(cancion["title"])

def mostrar_menos_visitas():
    minimo_reproducciones = 0
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False:
            bandera_primer_tema = True
            minimo_reproducciones = cancion["views"]
    for cancion in lista_bzrp:
        if cancion["views"] == minimo_reproducciones:
            print(cancion["title"])

def mostrar_suma_de_reproducciones():
    acumulador_reproducciones = 0

    for cancion in lista_bzrp:
        acumulador_reproducciones += cancion["views"]

    print(f"La cantidad total de reproducciones del canal es: {acumulador_reproducciones}")

def mostrar_promedio_de_reproducciones():
    promedio_reproducciones = 0

    for cancion in lista_bzrp:
        promedio_reproducciones += cancion["views"]

    promedio_reproducciones = promedio_reproducciones / len(lista_bzrp)

    print(f"El promedio de reproducciones del canal es: {(promedio_reproducciones/1000000):.2f} millones de reproducciones")

system("cls")
while True:
    respuesta = int(input("""
            1. mostrar temas
            2. Mostrar temas mas vistos
            3. Mostrar temas menos vistos 
            4. Mostrar suma de reproducciones
            5. Mostrar promedio de reproducciones
            10. Salir
            Elija una opcion: """))
     match respuesta:
        case 1:
            mostrar_temas()
        case 2:
            mostrar_el_maximo()
        case 3:
            mostrar_menos_visitas()
        case 4:
            mostrar_suma_de_reproducciones()
        case 5:
            mostrar_promedio_de_reproducciones()
        case 10:
            break"""

