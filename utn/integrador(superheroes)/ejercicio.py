from Data_stark import lista_personajes
from os import system
system("cls")

def mostrar_nombre_de_cada_heroe():
    for superheroe in lista_personajes:
        print(f"{superheroe['nombre']}")
        
def mostar_altura_de_cada_heroe():
    
    for superheroe in lista_personajes:
        print(f"{superheroe['nombre']}-- {superheroe['altura']}")

def mostrar_el_heroe_mas_alto():
    
    bandera_altura=True
    for superheroe in lista_personajes:
        
        if bandera_altura==True or float(superheroe["altura"]) > superheroe_mas_alto:
            bandera_altura=False
            superheroe_mas_alto= float(superheroe["altura"])
            nombre_del_alto=superheroe["nombre"]
            
    print(f"el mas alto es: {nombre_del_alto} y su altura es: {superheroe_mas_alto}")
        
def mostrar_el_heroe_mas_bajo():
    
    superheroe_mas_bajo=0
    bandera_menor=True

    for superheroe in lista_personajes:
        if bandera_menor == True or float(superheroe["altura"]) < superheroe_mas_bajo:
            bandera_menor=False
            superheroe_mas_bajo=float(superheroe["altura"])
            nombre_del_bajo=superheroe["nombre"]
        
    print(f"el nombre del mas bajo es: {nombre_del_bajo} y su altura es: {superheroe_mas_bajo}")

def mostrar_el_promedio_altura():
    
    acumulador_altura=0
    
    for superheroe in lista_personajes:
        acumulador_altura += float(superheroe["altura"])
        promedio_altura = acumulador_altura / len(lista_personajes)
    print(f"El promedio de la altura de los heores son:{promedio_altura} ")
         
def mostrar_el_heroe_mas_pesado_liviano():
    bandera_peso=False
    bandera_peso_min=True
    peso_maximo=0
    peso_minimo=0

    for superheroe in lista_personajes:
        if  float(superheroe["peso"]) >peso_maximo or bandera_peso == False:
            bandera_peso = True
            peso_maximo = float(superheroe["peso"])
            nombre_del_pesado = superheroe["nombre"]
        elif float(superheroe["peso"]) < peso_minimo or bandera_peso_min==True:
            bandera_peso_min=False
            peso_minimo=float(superheroe["peso"])
            nombre_del_liviano=superheroe["nombre"]
            
    print(f"el heroe mas pesado es: {nombre_del_pesado} y el liviano es: {nombre_del_liviano}")


        

    
    
while True:
    respuesta=int(input("""
            1. mostrar nombre de cada heroe
            2. Mostrar altura de cada heroe
            3. Mostrar el heroe mas alto 
            4. Mostrar mostrar el heroe mas bajo
            5. Mostrar promedio de altura de los heroes
            6. mostrarel heroe que mas y menos pesa
            7. Salir
            ELIJA UNA OPCION: """))
        
    if respuesta == 1 :
        mostrar_nombre_de_cada_heroe()
    elif respuesta == 2:
        mostar_altura_de_cada_heroe()
    elif respuesta == 3:
        mostrar_el_heroe_mas_alto()
    elif respuesta == 4:
        mostrar_el_heroe_mas_bajo()
    elif respuesta == 5:
        mostrar_el_promedio_altura()
        
    elif respuesta == 6:
        mostrar_el_heroe_mas_pesado_liviano()
        pass
    elif respuesta == 7:
        break
    

            


