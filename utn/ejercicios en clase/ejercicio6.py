#Crear una función que permita determinar si un número es par o no. 
# La función retorna 1 en caso afirmativo y 0 en caso contrario. Probar la funcion
respuesta="si"

def mostrar_numero_par():
    
    if numero %2 == 0:
        resultado = 1
        print(resultado)
    else:
        resultado = 0
        print(resultado)

while respuesta =="si":
    numero=int(input("ingrese un numero: "))
    
    mostrar_numero_par()
    
    #print(resultado)
    
    respuesta=input("queres ingresar otro numero?: ")
    
    