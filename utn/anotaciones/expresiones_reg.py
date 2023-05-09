import re

#split

#print(re.split(" ","hola mundo"))

#print(re.split("[a-z]" ,"hola 1c")) # excluye letras

#print(re.split("[0-9 ]", " hola1c")) # exluye numeros

print(re.split("hola|chau", " hola como estan ? chau")) # te saca las palabras


#### search

#print(re.search(" ", "texto")) # encuentra las coincidencias

#print(re.search("[0-9]+", "texto 123 bienvenido")) # muetra lsa coincidencias y en la posicion donde esta
#print(re.search("[0-9]+{1}", "texto 123 bienvenido")) # lo mismo pero le puse un limite
#print(re.search("e", "texto 123 bienvenido").start()) # donde empieza la ocurreencia
#print(re.search("e", "texto 123 bienvenido").end()) # donde termina

#######################################################

#find dall

'''texto= " uno 1 dos 25 tres 3 cuatro 4"

print(re.findall("[0-9]+",texto)) # muestra los numeros encontrados
print(re.findall("[a-z]+",texto))
'''

#####################################################

#sub

'''texto = "abc ddd ccc abc aaa"

resultado = re.sub("abc", "",texto) # remplaza elementos
print(resultado)

resultado = re.sub(r"/s+", "-",texto) # espacio duplicado te lo reemplaza por un gion medio'''
##############################################

texto = 'QUEVEDO || BZRP Music Sessions #52'

'''print(re.split("[||]+", texto)) #solucion uno

#print(re.split(" /|+ | #", texto))
print(re.split(" [| #]+",texto))

'''
fecha = "2022-02-03 19:23:45"

'''print(re.split(" ",fecha))
print(re.split("[0-9]{2}:[0-9]{2}:[0-9]{2}:",fecha))
#print(re.sub(" [0-9]{2}:"))
'''
print(re.findall("[0-9]{4}",fecha)) # solo año
print(re.findall("-([0-9]{2})-",fecha)) # solo mes


