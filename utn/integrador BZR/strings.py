'''{'title': 'QUEVEDO || BZRP Music Sessions #52', 
 'views': 227192970, 
 'length': 204, 
 'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
 'date': '2022-07-06 00:00:00'}

'''
from Data import lista_bzrp
from os import system
system("cls")

def prueba ():
    titulo='QUEVEDO || BZRP Music Sessions #52'
    parte_uno=titulo.split("||")
    artista = parte_uno[0].strip()

    parte_dos= parte_uno[1].split("#")
    tipo=parte_dos[0].strip()
    tipo=parte_dos[0].upper()
    numero= parte_dos[1]
    
    print(parte_dos)
    
    
    print(f"{artista}-{numero}-{tipo}")

def prueba1(titulo:str):
    #titulo='QUEVEDO || BZRP Music Sessions #52'
    parte_uno=titulo.split("||")
    if(len(parte_uno)>1):
        artista = parte_uno[0].strip()
        parte_dos= parte_uno[1].split("#")
        if (len(parte_dos)>1):
            tipo=parte_dos[0].strip()
            tipo=parte_dos[0].upper()
            numero= parte_dos[1]
        
            print(f"{artista}-{numero}-{tipo}")
 
def prueba2(titulo:str): 
    parte_uno=titulo.split("BZRP Music Sessions")
    print(parte_uno)
    if(len(parte_uno)==2):
        artista=parte_uno[0].replace("||","")
        print(artista)
                        
def formatear_titulo(lista:list):
    for tema in lista:
        prueba4(tema["date"])


def prueba3(url:str):
    #'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
    lista = url.split("=")
    print(lista[1])

def prueba4(fecha:str):
    #lista=date.splip("-")
    #año=lista
    fecha_split= fecha.split(" ")
    fecha_formato= fecha_split[0].split("-")
    año=fecha_formato[0]
    mes=fecha_formato[1]
    dia=fecha_formato[2]
    print(f"{año}-{mes}-{dia}")

respuesta=True       
while respuesta ==True:
    
    respuesta=int(input("""
                    opcion1: mostrar temas 
                    opcion 2: mostrar temas mas vistos 
                    opcion 3: mostrar temas menos vistos
                    opcion 4 mostrar suma de reproducciones
                    opcion 5 mostrar promedio de reproducciones
                    opcion 6 mostrar tema mas largo
                    opcion 7 normalizar datos
                    eliga una opcion: """))
    
    if respuesta == 1:
        #mostrar_temas(lista_bzrp)
        pass
    elif respuesta== 2:
        pass
        #mostrar_temas_con_mas_reproducciones(lista_bzrp)
        pass
    elif respuesta ==3:
        pass
    elif respuesta == 4:
        pass
    elif respuesta == 5:
        pass
    elif respuesta == 6:
        pass
        #mostrar_tema_mas_largo(lista_bzrp)
    elif respuesta == 7:
        formatear_titulo(lista_bzrp)
    elif respuesta == 8:
        break
                    


     



     






        




