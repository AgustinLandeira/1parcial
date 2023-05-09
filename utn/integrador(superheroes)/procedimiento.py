from Data_stark import lista_personajes
from os import system
system("cls")


for superheroe in lista_personajes:
        print(f"{superheroe['nombre']}")#b
        
for superheroe in lista_personajes:
        print(f"{superheroe['nombre']}-- {superheroe['altura']}")  









#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)


bandera_altura=True


for superheroe in lista_personajes:
    #altura_superheroe=float(superheroe["altura"])
    if bandera_altura==True or float(superheroe["altura"]) > superheroe_mas_alto:
        
        bandera_altura=False
        superheroe_mas_alto= float(superheroe["altura"])
        nombre_del_alto=superheroe["nombre"]
        
print(f"el mas alto es: {nombre_del_alto} y su altura es: {superheroe_mas_alto}")

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

superheroe_mas_bajo=0
bandera_menor=True

for superheroe in lista_personajes:
    if bandera_menor == True or float(superheroe["altura"]) < superheroe_mas_bajo:
        bandera_menor=False
        superheroe_mas_bajo=float(superheroe["altura"])
        nombre_del_bajo=superheroe["nombre"]
        
print(f"el nombre del mas bajo es: {nombre_del_bajo} y su altura es: {superheroe_mas_bajo}")

#F. Recorrer la lista y determinar la altura promedio de los superhéroes
#(PROMEDIO)
acumulador_altura=0

for superheroe in lista_personajes:
    acumulador_altura += float(superheroe["altura"])
    
promedio_altura = acumulador_altura / len(lista_personajes)
print(f"El promedio de la altura de los heores son:{promedio_altura} ")

#H. Calcular e informar cual es el superhéroe más y menos pesado.

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

###################################################################################################################
## ejercicio integrador 02
'''while True:
        respuesta= stark_menu_principal()
            
        if respuesta == 1 :
            stark_imprimir_nombres_heroes(lista_personajes)
            
        elif respuesta == 2:
            stark_imprimir_nombres_alturas(lista_personajes)
            
        elif respuesta == 3:
            valor=input("queres averiguar el minimo o maximo?:  ")
            tipo_dato=input("que queres averiguar?(altura,peso,etc) ")
            stark_calcular_imprimir_heroe(lista_personajes,valor,tipo_dato)
        
        elif respuesta == 4:
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        elif respuesta == 5:
            #mostrar_el_promedio_altura()
            nombre=input("ingrese el nombre del heroe: ")
            key=input("ingrese el dato que quiera saber: ")
            obtener_nombre_dato(nombre,key,lista_personajes)
            #rta=obtener_nombre_dato()
            #print(rta)
        elif respuesta == 6:
            #mostrar_el_heroe_mas_pesado_liviano()
            print(obtener_nombre_dato(lista_personajes[4],"inteligencia"))
        elif respuesta == 7:
            break
        elif respuesta == 8:
            stark_imprimir_nombres_alturas(lista_personajes)
        elif respuesta == 9:
            calcular_max_min_dato(lista_personajes,"minimo","peso")
        elif respuesta == 10:
            stark_calcular_imprimir_heroe(lista_personajes,"maximo","altura")
        elif respuesta == 11:
            #sumar_dato_heroe(lista_personajes,"altura")
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        elif respuesta == 12:
            mensaje = validar_entero(1)
            print(mensaje)
        
            
stark_marvel_app(lista_personajes)
                
                
        











'''



    

    



