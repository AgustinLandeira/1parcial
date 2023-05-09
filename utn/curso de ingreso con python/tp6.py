#Bienvenidos.
#Realizar el algoritmo que permita el ingreso por prompt de las notas (validar entre 0 y 10) 
# , el sexo (validar el sexo “f” o “m”) de 5 alumnos, informar por alert:
#a) El promedio de las notas totales.
#b) La nota más baja y el sexo de esa persona.
#c) La cantidad de varones que su nota haya sido mayor o igual a 6.

acumulador_notas=0
contador_notas=0
bandera_primero=True
contador_masculino=0

for i in range (5):
    
    nota=int(input("ingrese la nota del alumno: "))
    while nota<0 or nota>10:
        nota=int(input("ERROR EL NUMERO ESTA FUERA DE RANGO(validar entre 0 y 10):  "))
        
    sexo=input("porfavor ingrese su sexo (masculino o femenino): ")
    while sexo!="masculino" and sexo !="femenino":
        sexo=input("porfavor ingrese su sexo otra vez (masculino o femenino): ")
        
    contador_notas=contador_notas+1
    acumulador_notas+=nota
    
    if bandera_primero==True:
        nota_minima=nota
        sexo_de_la_nota_baja=sexo
        bandera_primero=False
    elif nota<nota_minima:
        nota_minima=nota
        sexo_de_la_nota_baja=sexo
        
    if nota>=6 and sexo=="masculino":
        contador_masculino=contador_masculino+1
          

promedio=acumulador_notas/contador_notas
print(f"el promedio de las notas son: {promedio}")    
print(f"la nota mas baja fue: {nota_minima} y su genero es: {sexo_de_la_nota_baja}")
print(f"la cantidad de chicos que se sacaro mas de seis fueron: {contador_masculino}")