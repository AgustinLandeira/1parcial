'''4.Reemplazar formato de fecha: Crea una función que tome una cadena de texto que
contiene una fecha en formato dd/mm/aaa; y la reemplace por la misma fecha en
formato mm/dd/aaaa'''
import re
fecha = input("ingresar una fecha con el formato(dd/mm/aaa): ")

def reemplazar_fecha(fecha:str):
    
    if re.match("[0-9]{2}/[0-9]{2}/[0-9]{4}",fecha):
        fecha_nueva = fecha.split("/")
        dia = fecha_nueva[0]
        mes = fecha_nueva[1]
        año = fecha_nueva[2]
        print(f"{mes}/{dia}/{año}")
    else:
        print("fecha no valida")
    
    
    
    
    
reemplazar_fecha(fecha)