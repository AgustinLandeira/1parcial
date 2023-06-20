'''1.Verificar correo electrónico: Crea una función que tome una cadena de texto como
argumento y verifique si se trata de una dirección de correo electrónico válida. Una
dirección de correo electrónico válida debe tener un formato como
usuario@dominio.com'''
import re
cadena=input("ingrese el mail: ")

def validar_cadena(cadena:str):
    if re.match('^([a-z-Z0-9]+@[a-zA-Z]+\.[com])',cadena):
        print("el mail es correcto")
    else:
        print("el mail es incorrecto")
    
validar_cadena(cadena)   
 


