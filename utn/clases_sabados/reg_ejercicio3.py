'''3.Validar formato de fecha: Crea una función que tome una cadena de texto como
argumento y verifique si se trata de una fecha válida en formato dd/mm/aaaaa'''
import re

fecha = input("ingrese una fecha con este formato(dd/mm/aaaaa): ")
def verificar_fecha(fecha:str):
    
    if re.match("[0-9]{2}/[0-9]{2}/[0-9]{4}",fecha):
        print("la fecha es valida")
    else:
        print("no es valida")
        
verificar_fecha(fecha)