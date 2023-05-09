"""2-
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta. """

from os import system
system("cls")

respuesta="si"
lista_diccionario=[]
lista_español=[]
lista_ingles=[]


while respuesta=="si":
    palabra=input("ponga la palabra en español: ")
    palabra_ingles=input("ponga la palabra traducida en ingles: ")
    
    diccionario={"palabra en español":palabra, "palabra en ingles": palabra_ingles}
    
    lista_diccionario.append(diccionario)
    lista_ingles.append(palabra_ingles)
    lista_español.append(palabra)
    
    if lista_español.count(palabra) >1: 
        for repetido in lista_español:
            if palabra == repetido:
                print("no se puede agregar este elemento en la lista, porque esta en la posicion", end=": ")
                print(lista_español.index(repetido)+1)
    if lista_ingles.count(palabra_ingles):
        for repeticion in lista_español:
            if palabra_ingles == repeticion:
                print("no se puede agregar este elemento en la lista, porque esta en la posicion", end=": ")
                print(lista_ingles.index(repetido)+1)
   
    respuesta=input("queres ingresar otra palabra?: ")

for palabras in lista_diccionario:
    
    print(f"la palabra en español es: {palabras['palabra en español']} y en ingles: {palabras['palabra en ingles']}")
       

  
  
  
  
""" if diccionario.get(palabra) != None:
        print(palabra,diccionario.get(palabra))
    
    
    if diccionario.get(palabra) == None :
        traduccion=input("ingrese la traduccion en ingles: ")
        diccionario.update({palabra:traduccion})
        lista_diccionario.append(una_palabra)
        print("la palabra se agrego al diccionario")
    else :
        print("la palabra ya esta en el diccionario")  """  