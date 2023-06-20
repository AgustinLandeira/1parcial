'''2.Eliminar dígitos: Crea una función que tome una cadena de texto y elimine todos los
dígitos que contiene.'''
import re
cadena = input("ingrese la cadena de texto: ")
def eliminar_digitos(cadena:str):
    print(re.sub("[0-9]","",cadena))
eliminar_digitos(cadena)