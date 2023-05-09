diccionario={
    "nombre":"soy agus",
    "apellido":"landeira",
    "subs": 30
} 

numeros=[1,2,3,4,5,6,7]

cadena= "hola agus"
# recorriendo un diccionario con items para tener la clave y el valor
"""for datos in diccionario.items():
    key = datos[0]
    value=datos[1]
    print(f"la clave es: {key} y el value : {value}")"""
    
frutas = ["banana","durazno","manzana","ciruela","pera","granada","manzanaverde"]
#evitamos que se coma una granada con la setencia continue
"""for fruta in frutas:
    if fruta  == "granada" :
        continue
        
    print(f"me voy a comer una: {fruta}")"""
 #evitar que el bucle no se ejecute   
"""for fruta in frutas:
    if fruta  == "granada" :
        break
        """

"""for letra in cadena:
    print(letra)"""

for numero in numeros:
    numero_duplicado=numero*2
    print(numero_duplicado)
