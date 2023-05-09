#debemos realizar la carga de 5(cinco) productos de prevención de contagio,
#de cada una debo obtener los siguientes datos:
#l tipo (validar "barbijo" , "jabón" o "alcohol") ,
##l precio (validar entre 100 y 300),
#la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades),
#la Marca y el fabricante.
#Se debe Informar al usuario lo siguiente:
#a) Del más barato de los alcohol, la cantidad de unidades y el fabricante
#b) Del tipo con mas unidades, el promedio por compra
#c) Cuántas unidades de jabones hay en total

bandera_primero=True
acumulador_unidades_barbijo=0
acumulador_unidades_jabon=0
acumulador_unidades_alcohol=0
total_jabon=0
total_alcohol=0
total_barbijo=0
contador_jabon=0
contador_barbijo=0
contador_alcohol=0

for i in range(5):
    
    tipo=input("que tipo queres tener?(elegir barbijo , jabón o alcohol) : ")
    while tipo !="barbijo" and tipo!="jabon" and tipo !="alcohol":
        tipo=input("ERROR,(elegir barbijo , jabón o alcohol) : ")
    precio=int(input("ponga el precio del producto: "))
    while precio<100 or precio>300:
        precio=int(input("ERROR ponga el precio del producto (entre 100 y 300): "))
    cantidad_unidades=int(input("ponga la cantidad de unidades: "))
    while cantidad_unidades<0 or cantidad_unidades>1000:
        cantidad_unidades=int(input("ERROR, ponga la cantidad de unidades en el rango: "))
    marca=input("escriba la marca que eligio: ")
    fabricante=input("ingrese el fabricante: ")
    
    if tipo =="alcohol":
        if(bandera_primero==True):
            precio_minimo=precio
            unidades_del_alcohol_barato=cantidad_unidades
            fabricante_del_alcohol=fabricante
            bandera_primero=False
            acumulador_unidades_alcohol+=cantidad_unidades
            contador_alcohol=contador_alcohol+1
            total_alcohol+=cantidad_unidades*precio
        elif precio<precio_minimo:
            precio_minimo=precio
            unidades_del_alcohol_barato=cantidad_unidades
            fabricante_del_alcohol=fabricante
            acumulador_unidades_alcohol+=cantidad_unidades
            contador_alcohol=contador_alcohol+1
            total_alcohol+=cantidad_unidades*precio
        else:
            acumulador_unidades_alcohol+=cantidad_unidades
            contador_alcohol=contador_alcohol+1
            total_alcohol+=cantidad_unidades*precio
            
    elif tipo =="barbijo":
        acumulador_unidades_barbijo+=cantidad_unidades
        contador_barbijo=contador_barbijo+1
        total_barbijo+=cantidad_unidades*precio
    else:
        acumulador_unidades_jabon+=cantidad_unidades
        contador_jabon=contador_jabon+1
        total_jabon+=cantidad_unidades*precio


if (acumulador_unidades_alcohol>acumulador_unidades_barbijo and 
   acumulador_unidades_alcohol>acumulador_unidades_jabon):
    promedio=total_alcohol/contador_alcohol
elif acumulador_unidades_barbijo>acumulador_unidades_jabon:
    promedio=total_barbijo/contador_barbijo
else:
    promedio=total_jabon/contador_jabon
    

print(f"""la cantidad de unidades del alcohol mas barato es de :{unidades_del_alcohol_barato} y su fabricante fue: 
      {fabricante_del_alcohol}""")
print(f"el promedio de compra del que tiene mas unidades es de un : {promedio}")
print(f"la cantidad de unidades de jabones en total son: {acumulador_unidades_jabon}")