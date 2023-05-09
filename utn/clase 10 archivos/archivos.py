from os import system
system("cls")   

'''path= "nombre.txt"

archivo_texto = open(path,"a")

archivo_texto.write("agus") # paara escribir algo
archivo_texto.close()
'''

'''path = "nombre.txt"

archivo_texto = open(path,"r")
lectura = archivo_texto.read()
print(lectura)
archivo_texto.close()'''
##############################################
'''path = "nombre.txt"

archivo_texto = open(path,"r")
lista = archivo_texto.readlines()   # me muestra una lista
print(lista)
archivo_texto.close()
    
for linea in lista:
    print(linea,end="") # me imprime la lista'''
##################################################
lista=["gio","agus","lucas"]

archivo = open("nombres.txt","w")

for nombre in lista: #creo una lista y la paso a un archivo
    archivo.write(f"{nombre}\n")
archivo.close()

path = "nombres.txt"

archivo_texto = open(path,"r")
lista = archivo_texto.readlines()   # me muestra una lista
print(lista)
archivo_texto.close()
    
for linea in lista:
    print(linea,end="") 
###########################################################
#csv

'''nombres = ["jose","maria","franco"]
apellidos = ["gomez","ruiz","perez"]
edades= [23,36,47]

with open("agende.csv","w") as archivo:
    for i in range(3):
        line="{0},{1},{2}\n".format(nombres[i],apellidos[i],edades[i])
        archivo.write(line)
        '''
'''import re

with open("agende.csv","r") as archivo:
    for line in archivo:
       #registro = line.split(",")
       registro = re.split(",|\n",line)
       #print(registro)
       
       print(f"{registro[0]}-{registro[1]}-{registro[2]}")
       
       '''
###################################################
#json
'''import json

data = {}

data["clientes"] = []

data["clientes"].append({"nombre":"juan","edad":25})
data["clientes"].append({"nombre":"maria","edad":30})
data["clientes"].append({"nombre":"luis","edad":42})

with open("clientes.json","w") as archivo:
    json.dump(data,archivo, indent=4)
'''
'''with open("clientes.json","r") as archivo:
    mi_data= json.load(archivo)
print(mi_data)
'''
#######################################parser################################
'''import re
def parser_csv(path:str)->list:
    lista_temas=[]
    print("estoy adentro")
    archivo = open(path,"r",encoding="UTF-8")
    for line in archivo:
        registro = re.split(",|\n",line)
        
        tema={}
        tema["title"]= registro[0]
        tema["seccion"]= registro[1]
        tema["views"]= registro[2]
        tema["img_url"]= registro[3]
        tema["url"]= registro[4]
        tema["date"]= registro[5]
        
        lista_temas.append(tema)
    
    return lista_temas


lista_biza = parser_csv("bzr.csv")
for tema in lista_biza:
    print(f"{tema['views']}")
'''
  