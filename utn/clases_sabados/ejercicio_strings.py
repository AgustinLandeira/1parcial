
def contar_letras(cadena:str):
    "cuento los caracteres de la cadena"
    print(len(cadena))
    
def eliminar_caracteres(cadena:str,caracter:str):
    
    nueva_cadena=cadena.replace(caracter,"")
    print(nueva_cadena)
    
def contar_palabras(cadena:str):
    
    palabras = cadena.split(" ")
    cantidad = len(palabras)
    print(cantidad)
    

def reemplazar_palabras(cadena:str,primer_palabra:str,segunda_palabra:str):
    
    nueva_cadena=cadena.replace(primer_palabra,segunda_palabra)
    print(nueva_cadena)
    
def buscar_segunda_palabra(primer_cadena:str,patron:str):
    pass
