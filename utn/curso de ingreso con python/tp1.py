#Se debe realizar la carga de 5 ventas de productos de almacen, los datos a cargar de cada uno son:

#marca (validar que se ingrese un dato)
#precio (entre 300 y 2000)
##tipo (yerba, azucar, galletitas)
#Informar lo siguiente:

#El monto total vendido de yerba.
#La marca y cantidad de unidades del azucar mas barato.
#del tipo con mas unidades vendidas el promedio de cada compra.

seguir="si"
monto_total_yerba=0
monto_total_azucar=0
monto_total_galletitas=0
bandera_primero=True
acumulador_unidades_yerba=0
acumulador_unidades_azucar=0
acumulador_unidades_galletitas=0
contador_azucar=0
contador_yerba=0
contador_galletitas=0


for i in range(5):
    marca= input(" ingrese la marca: ")
    
    precio_del_producto=int(input("ingrese el precio del producto(ENTRE 300 Y 2000): "))
    while(precio_del_producto <300 or precio_del_producto>2000):
        precio_del_producto=int(input("ERROR, ingrese el precio del producto: "))
   
    tipo=input("ingrese el tipo de prducto que quiera(yerba, azucar, galletitas): ") 
    while(tipo !="yerba" and tipo !="azucar" and tipo !="galletitas") :
        tipo=input("ERROR, ingrese el tipo de prducto que quiera(yerba, azucar, galletitas): ")
    unidades=int(input("cuantas unidades queres comprar?"))
     
    if tipo=="yerba":
        monto_total_yerba+= unidades* precio_del_producto
        acumulador_unidades_yerba=acumulador_unidades_yerba+unidades
        contador_yerba=contador_yerba+1
        
    elif tipo=="azucar" :
        if bandera_primero==True:   
            precio_minimo=precio_del_producto
            unidades_del_menor_precio=unidades
            bandera_primero=False
            acumulador_unidades_azucar+=acumulador_unidades_azucar+unidades
            monto_total_azucar+=unidades* precio_del_producto
            contador_azucar=contador_azucar+1
        else:
            if precio_del_producto<precio_minimo:
              precio_minimo=precio_del_producto
              unidades_del_menor_precio=unidades
              acumulador_unidades_azucar+=acumulador_unidades_azucar+unidades
              monto_total_azucar+=unidades* precio_del_producto
              contador_azucar=contador_azucar+1
            else:
                acumulador_unidades_azucar+=acumulador_unidades_azucar+unidades
                monto_total_azucar+=unidades* precio_del_producto
                contador_azucar=contador_azucar+1
    else:
        acumulador_unidades_galletitas=acumulador_unidades_galletitas+unidades  
        monto_total_galletitas+=unidades* precio_del_producto  
        contador_galletitas=contador_galletitas+1   
              
              
    seguir=input("desea comprar otra vez?: ") 
    
if(acumulador_unidades_azucar>acumulador_unidades_galletitas and acumulador_unidades_azucar>
   acumulador_unidades_yerba) :
    promedio=monto_total_azucar/contador_azucar  
elif(acumulador_unidades_galletitas>acumulador_unidades_yerba)  :
    promedio=monto_total_galletitas/contador_galletitas
else:
    promedio=monto_total_yerba/contador_yerba    
             
print(f"el monto total de yerba es: {monto_total_yerba}")
print(f"el precio del azucar mas barato es de {precio_minimo}pesos y sus unidades {unidades_del_menor_precio}")
print(f"el promedio de compra del tipo que tiene mas unidades es de: {promedio} ")