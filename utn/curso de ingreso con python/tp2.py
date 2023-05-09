#Tipo ("arena", "cal", "cemento")
#Cantidad de bolsas
#Precio por bolsa (entre 1000 y 3000 )
#Para calcular el importe total se debe saber lo siguiente:
#Si el monto de la compra supera los $15000 obtiene un descuento de 10%.
#Si el monto de la compra supera los $25000 obtiene un descuento de 15%.

#Si el monto de la compra (con descuento) es menor a $14000 se le suma el 21% de iva.
#Si el monto de la compra (con descuento) es mayor o igual a $14000 se le suma el 10% de IVA.
#Informar lo siguiente:

#Informar el importe total a pagar (con IVA).
#El tipo mas caro (sin descuento ni IVA).
#Informar el tipo de la compra de mayor monto (sin descuento ni IVA).
#Informar el monto total a pagar (con descuento e IVA).


seguir="si"
acumulador_monto=0
bandera_primero=True
montmonto_total_arena=0
monto_total_cemento=0
monto_total_cal=0
while seguir=="si":
    tipo=input("eliga el tipo (arena, cemento, cal)")
    while tipo !="arena" and tipo !="cemento" and tipo !="cal":
        tipo=input("ERROR ,eliga el tipo (cemento, cal, arena)")
        
    cantidad_de_bolsas= int(input ("ingrese la cantidad de bolsas: "))
    
    precio_por_bolsa=int(input("ingrese  precio por bolsa"))
    while(precio_por_bolsa<1000 or precio_por_bolsa>3000):
        precio_por_bolsa=int(input(" ERROR ingrese  precio por bolsa"))
    
    acumulador_monto += cantidad_de_bolsas*precio_por_bolsa
    
    if bandera_primero==True:
        bandera_primero=False
        precio_max=precio_por_bolsa
        tipo_mas_caro=tipo
    else:
        if precio_por_bolsa>precio_max:
             precio_max=precio_por_bolsa
             tipo_mas_caro=tipo
             
    if tipo=="arena":
       montmonto_total_arena+=cantidad_de_bolsas*precio_por_bolsa
    elif tipo=="cal":
        monto_total_cal+=cantidad_de_bolsas*precio_por_bolsa
    else: 
        monto_total_cemento=cantidad_de_bolsas*precio_por_bolsa
    
    seguir=input("desea comprar mas materiales?: ")
    
    
    
if acumulador_monto>25000:
    monto_con_descuento=acumulador_monto*0.85
else:
    if acumulador_monto>15000:
        monto_con_descuento=acumulador_monto*0.9
    else:
        monto_con_descuento=acumulador_monto

if monto_con_descuento<14000:
    monto_iva=monto_con_descuento*1.21
else:
    if monto_con_descuento>=14000:
       monto_iva=monto_con_descuento*1.21    
           

if(monto_total_cemento>montmonto_total_arena and monto_total_cemento>monto_total_cal):
    mayor_monto="cemento"
elif(monto_total_cal>montmonto_total_arena) :
    mayor_monto="cal"   
else :
    mayor_monto="arena"
print(f"el importe total a pagar es {monto_iva}")
print(f"el tipo mas caro es {tipo_mas_caro}")
print (f"el tipo con mayor monto es: {mayor_monto}")        