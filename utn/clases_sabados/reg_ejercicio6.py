'''6.Validar CUIL: Escribe una expresión regular que valide un CUIL con el siguiente
formato: 20-12345678-1. La expresión regular debe aceptar CUILS que comiencen con
20; seguido de un guión, ocho dígitos y otro guión, seguido del último dígito que es un
verificador.'''
import re
cuil = input("ingrese su cuil: ")

def validar_cuil(cuil):
    
    if re.match("^20-\d{8}-1",cuil):
        print("cuil correcto")
    else:
        print("incorrecto")
        
validar_cuil(cuil)



