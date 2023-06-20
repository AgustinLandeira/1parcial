"""3-
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista."""

"""lista=[]

respuesta="si"

while respuesta=="si":
    numero=int(input("ingrese un numero: "))
    
    lista.append(numero)
    
    respuesta=input("queres agregar otro numero?: ")
 
   
print(id(lista.index(9)))"""

#frecuencias = Counter(numeros)
#elemento_mas_comun = frecuencias.most_common(1)[0][0]
numeros = []
while True:
    numero = input("Introduce un número (o presiona Enter para salir): ")
    if numero == "":
        break
    numeros.append(int(numero))

# Contamos las ocurrencias de cada posición de memoria
ocurrencias = {}
for i in range(len(numeros)):
    if numeros[i] not in ocurrencias:
        ocurrencias[numeros[i]] = [i]
    else:
        ocurrencias[numeros[i]].append(i)

# Buscamos la posición de memoria con más ocurrencias
posicion_mas_ocurrencias = None
max_ocurrencias = 0
for posicion, lista_posiciones in ocurrencias.items():
    num_ocurrencias = len(lista_posiciones)
    if num_ocurrencias > max_ocurrencias:
        posicion_mas_ocurrencias = lista_posiciones[0]
        max_ocurrencias = num_ocurrencias

print("La posición de memoria que más ocurrencias tiene es:", posicion_mas_ocurrencias)
