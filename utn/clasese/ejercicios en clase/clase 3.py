

"""lista=[1,2,3,4,5,6,5]
print(lista)

print(f"el elemento 3 es: {lista [3]}")
print(lista[0:3])#desde hasta   inclusivo/exclusivo
print(lista[3:5])

acumulador=0
contador=0

for i in range(len(lista)):
    acumulador= acumulador + lista[1]
    
    if(lista[i] == 5):
        contador += 1
print(acumulador)  
print(contador)  

lista.append(100) #agrega un elemento
print(lista)

lista.insert(2,999) #reemlaza el valor (indice,valor)
print(lista)

lista.extend([100,200,300]) #agrega varios elementos
print(lista)

lista.remove(5)
print(lista)

print(lista.index(2)) #muestra en que indice esta"""

######################################################################################################
"""mi_diccionario = {}

mi_diccionario["nombre"] ="juan"
print(mi_diccionario["nombre"])

mi_diccionario["edad"] =25
print(mi_diccionario["edad"])

print(mi_diccionario)

otro_diccionario= {"nombre":"luis","edad":32}
print(otro_diccionario)

for key in otro_diccionario:
    print(key)
    print(otro_diccionario[key])"""
    
####################################################################################################
"""cantidad_alumnos=2

lista_nombres = []
lista_apellidos = []

for i in range(cantidad_alumnos):
    nombre= input("ingrese un nombre: ")
    apellido=input("ingrese apellido: ")
    
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)
    
for i in range (cantidad_alumnos):
    print(f"{i+1})nombre: {lista_nombres[i]} -apellido: {lista_apellidos[i]} ")"""
    
#################################################################################################################################

""""lista_alumnos = [   
    {"nombre":"juan","apellido":"ruiz",edad":25},
    {"nombre":"luis","apellido":"perez","edad":36},
    {"nombre":maria,"apellido":"ruiz","edad":23}
    }
]"""#hardcodeada

lista_alumnos = []
cantidad_alumnos = 3

for i in range(cantidad_alumnos):
    nombre= input("ingrese un nombre: ")
    apellido=input("ingrese apellido: ")
    edad=int(input("ingrese edad: "))
    un_alumno={}
    un_alumno["nombre"] = nombre
    un_alumno["apellido"] = apellido
    un_alumno["edad"] = edad
    lista_alumnos.append(un_alumno)
    
for alumno in lista_alumnos:
    apellido=alumno["apellido"]
    nombre=alumno["nombre"]
    edad=alumno["edad"]
    
    if edad>30:
        print(f"{apellido}-{nombre}-{edad}")


    
    
print(lista_alumnos)
    
    