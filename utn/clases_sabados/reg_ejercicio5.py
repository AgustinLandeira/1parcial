'''5.Validar número de teléfono: Escribe una expresión regular que valide un número de
teléfono con el siguiente formato: +54 9 11 1234-5678. La expresión regular debe
aceptar números de teléfono con el código de país +54, seguido de un espacio, el
dígito 9, otro espacio, el código de área de dos dígitos, un espacio, el número de
teléfono de ocho dígitos separado por un guión en la mitad.'''
import re

numero_telefono = input("ingrese el numero: ")

def validar_numero(numero:str):
    if re.match ('^\+54 9 \d{2} \d{4}-\d{4}$',numero):
        print("el numero es correcto")
    else:
        print("error")

validar_numero(numero_telefono)

