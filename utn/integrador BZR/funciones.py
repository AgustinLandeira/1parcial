""" 
def mostrar_temas():
    #b imprimir cada video
    for cancion in lista_bzrp:
            print(f"{cancion['title']}")
"""

def mostrar_temas(lista_bzrp:list):
    for cancion in lista_bzrp:
        mostrar_video(cancion)

def mostrar_algunos_temas(lista_bzrp:list,clave:str,valor:int):
        for cancion in lista_bzrp:
            if cancion[clave] == valor:
                mostrar_video(cancion)
            
def mostrar_video(un_video:dict):
    print(f"titulo: {un_video['title']}-",
          f"vistas: {un_video['views']}-",
          f"tiempo{un_video['length']}")