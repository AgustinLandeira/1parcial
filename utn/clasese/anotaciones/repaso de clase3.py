from os import system
system("cls")
"""lista= [5,9,8,7,3,6,4,5,5]
print(lista)
print(f"elemento 3: {lista[3]}")
print(lista[0:3])
print(lista[3:5])

acumulador=0
contador=0

for i in range(len(lista)):
    #print(lista[i])
    acumulador=acumulador+lista[i]
    if (lista[i] == 5):
        contador+=1
print(acumulador)
print(contador)

lista.append(100)
lista.append(55)
print(lista)

lista.insert(2,999)#remplaza el indice por el valor
print(lista)

lista.extend([999,888,777])
print(lista)

lista.remove(8) #elimina un elemento
print(lista)

print(lista.index(999)) # me dice en que indice esta el elemento

for numero in lista: #recorre la lista(los elementos)
    print(numero)"""

###########################################################################################

"""lista=[5,10,15,20]

for i in range(len(lista)):
    print(f"{i+1}->{lista[i]}")"""
###############################################################################
"""
mi_diccionario={}

mi_diccionario["nombre"] = "juan"
print(mi_diccionario["nombre"])
mi_diccionario["edad"] = 25
print(mi_diccionario["edad"])
print(mi_diccionario)

otro_diccionario = {"nombre":"luis","edad": 32}
print(otro_diccionario)

for key in otro_diccionario:
    print(key)
    
for key in otro_diccionario:
    print(otro_diccionario[key])"""
####################################################################
#listas pararelas
"""cantidad_alumnos=3
lista_nombres=[]
lista_apellidos=[]

for i in range(cantidad_alumnos):
    nombre=input("ingrese  nombre: ")
    apellido=input("ingrese apellido: ")
    
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)
    
    
for i in range(cantidad_alumnos):
    print(f"{i+1} NOMBRE: {lista_nombres[i]}- APELLIDOS {lista_apellidos[i]}")"""
####################################################################################################
'''cantidad_alumnos=3
lista_alumnos = []

for i in range(3):
    nombre=input("ingrese  nombre: ")
    apellido=input("ingrese apellido: ")
    edad=input("ingrese edad: ")
    
    un_alumno={}
    un_alumno["nombre"]=nombre
    un_alumno["apellido"]=apellido
    un_alumno["edad"]=edad
    
    lista_alumnos.append(un_alumno)
print(lista_alumnos)

for alumno in lista_alumnos:
    print(f" los alumnos se llaman: {alumno['nombre']}-apellido: {alumno['apellido']}")
'''

lista = ["agus","mauro"]
cadena="+"
print(cadena.join(lista))