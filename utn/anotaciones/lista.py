# indexacion
"""lista=["messi","neymar","cr7","mbappe","gavi"]
print(lista)

ultima_posicion=lista[-1]
print(ultima_posicion)

penultima_posicion=lista[-2]
print(penultima_posicion)

sublistas=lista[1:4]
print(sublistas)"""
########################################################################################
#comprobar si una lista tuiene un elemento o no

"""lista=["messi","neymar","cr7","mbappe","gavi"]

palabra="gavi"
palabra_dos="haland"

if palabra_dos in lista:
    print(f"esta en la lista: {palabra}")
else:
    print(f"{palabra_dos} no esta en lista")"""
########################################################################################
#modificar elementos de una lista

"""lenguajes=["c","java","javascrip","python","kotliyn"]

lenguajes[1]="angular"
print(lenguajes)

lenguajes[0]=lenguajes[0] + "++"
print(lenguajes)"""

################################################################################
"""
lenguajes=["c","java","javascrip","python","kotliyn"]
#print(lenguajes)
lenguajes.insert(1,"c++")
#print(lenguajes)

lenguajes.append("typesscript")
#print(lenguajes)

lenguaje_dos=["indepediente","boca","racing"]
lenguaje_dos.extend(lenguajes)
print(lenguaje_dos)

lenguaje_dos.remove("indepediente")
print(lenguaje_dos)"""
#############################################################################################

keywords=[]
ocurrencias=[]


for x in range(5):
    keyword=input("ingrese una clave o ponga fin para terminar: ")
    
    if keyword == "fin" :
        break
    else:
        keywords.append(keyword)
print(keywords)

