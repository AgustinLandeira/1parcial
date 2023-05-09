"""1-
Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código."""

from os import system
system("cls")

lista_autos=[]
respuesta="si"

while respuesta == "si":
    marca=input("ingrese la marca del auto: ")
    año_modelo=int((input("ingrese el año del modelo: ")))
    while año_modelo <0:
        año_modelo=int((input("ERROR,ingrese el año del modelo: ")))
        
    precio=int(input("ingrese el precio del auto: "))
    while precio <0:
        precio=int(input("ERROR,ingrese otravez el numero: "))
    
    un_auto={}
    un_auto["marca"]=marca
    un_auto["año del modelo"]=año_modelo
    un_auto["precio"]=precio
    
    lista_autos.append(un_auto)
    
    
    respuesta=input("queres ingresar los datos de otro auto?: ")

print(lista_autos)
    

for un_auto in lista_autos:
    marca=un_auto["marca"]
    año_modelo=un_auto["año del modelo"]
    precio=un_auto["precio"]
    
    print(f"""la marca es: {un_auto['marca']}
          el año del modelo es: {un_auto['año del modelo']}
          el precio del auto es: {un_auto['precio']}""")
    print("\n------------------------------------------------------------\n")