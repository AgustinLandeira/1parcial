#La división de alimentos está trabajando en un pequeño software para cargar las
#compras de ingredientes para la cocina de Industrias Wayne.
#Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
#para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
#de ingredientes.
#Se registra por cada compra:
#31. PESO: (entre 10 y 100 kilos)
#2. PRECIO POR KILO: (mayor a 0 [cero]).
#3. TIPO VARIEDAD: (vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
#descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
#de descuento sobre el precio bruto.
#Se desea saber:
#A. El importe total a pagar, BRUTO sin descuento.
#B. El importe total a pagar con descuento (Solo si corresponde).
#C. Informar el tipo de alimento más caro.
#D. El promedio de precio por kilo en total.

acumulador_kilos=0
acumulador_importe=0
bandera_primero=True


seguir="si"

for i in range(15):
    peso_compra= float(input(" ingrese el peso de la compra: "))
    while peso_compra<10 or peso_compra >100 :
        peso_compra= float(input("ERROR, el peso tiene que ser entre 10 y 100 kilos: "))
    
    precio_por_kilo=int (input("ingrese el precio por kilo: "))  
    while  precio_por_kilo <0:
        precio_por_kilo=int (input("ERROR,ingrese el precio por kilo devuelta: ")) 
     
    tipo_variedad=input("eliga el tipo (vegetal, animal, mezcla)")
    while tipo_variedad !="vegetal" and tipo_variedad !="animal" and tipo_variedad !="mezcla":
        tipo_variedad=input("ERROR ,eliga el tipo (vegetal, animal, mezcla)")
    
    acumulador_kilos+=peso_compra
    acumulador_importe+=peso_compra*precio_por_kilo
    
    if(bandera_primero==True):
        precio_maximo=precio_por_kilo
        tipo_mas_caro=tipo_variedad
        bandera_primero=False
    else:
        if precio_por_kilo>precio_maximo:
            precio_maximo=precio_por_kilo
            tipo_mas_caro=tipo_variedad
    
    

if acumulador_kilos>100 and acumulador_kilos <=300:
    importe_con_descuento=acumulador_importe*0.85
else:
    if acumulador_kilos>300:
        importe_con_descuento=acumulador_importe*0.75
        
    else:
          importe_con_descuento=acumulador_importe  
          
        
promedio= float(acumulador_importe/15)

print(f"el importe sin descuento es: {acumulador_importe} pesos")
print(f"el importe con descuento es: {importe_con_descuento} pesos ")
print(f"el tipo mas caro es: {tipo_mas_caro}")
print(f"el promedio por compra de un: {promedio}")
