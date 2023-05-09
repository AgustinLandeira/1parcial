from Data_stark import lista_personajes
from os import system
system("cls")

def extraer_iniciales(nombre_heroe:str):
    mensaje=""
    nombre_heroe=nombre_heroe.replace("-"," ")
    partes=nombre_heroe.split(" ") 
    if nombre_heroe != "":            
        for inicial in partes:
            inicial =inicial[0]
            if inicial == "t":
                pass
            else:    
                mensaje += inicial + "."
        return mensaje
    else:
        return("N/A")
    
def definir_iniciales_nombre(heroe:dict):
    if type(heroe)== dict:
        heroe["iniciales"]=extraer_iniciales(heroe["nombre"])
    
        mensaje = True
    else:
        mensaje= False
        
    return mensaje
                                                       
def agregar_iniciales_nombre(lista_heroes:list):
    
    if type(lista_heroes) == list and len(lista_heroes) >0:
        for heroe in lista_heroes:
            retorno=definir_iniciales_nombre(heroe)
            
            if retorno == False :
                print("El origen de datos no contiene el formato correcto")
                
    else:
        print("la lista esta vacia")
        
    return retorno                                                              

def star_imprimir_nombres_iniciales(lista_heroes:list):
    
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        iniciales=agregar_iniciales_nombre(lista_heroes)
        if iniciales == True:
            for heroe in lista_heroes:
                print(f"{heroe['nombre']}({heroe['iniciales']})")
                
def generar_codigo_heroe(id_heroe:int,genero_heroe:str):
    if type(id_heroe)== int and genero_heroe == "F" or genero_heroe == "M" :
        id=str(id_heroe)
        print (f"{genero_heroe}-{id.zfill(8)}")   
        
    elif genero_heroe =="NB" and type(id_heroe)==int:
        id=str(id_heroe)
        retorno (f"{genero_heroe}-{id.zfill(7)}")        
    
    else:
        retorno="N/A"

    return retorno

def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    mensaje = False
    
    if dict != None:
        heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe,heroe["genero"])
        
        if len(heroe["codigo_heroe"]) == 10:
            mensaje = True
    
    return mensaje

def stark_generar_codigos_heroes(lista_heroes:list): ######################
    contador = 0
    for heroe in lista_heroes:
        
        if agregar_codigo_heroe(heroe,contador + 1) == True:
            contador += 1
            
        else:
            print("error")
            break
    print(f"se asignaron {contador} generados ")
    
    
def sanitizar_entero(numero_str:str):
    numero_str=numero_str.strip()
    valor=""
    
    booleano=numero_str.isalpha()
    if booleano == True:
        valor=-1
    
    if numero_str[0]== "-":
        valor=-2
       
    booleano=numero_str.isdigit()
    
    if booleano == True:
        valor=int(numero_str)
        
    elif valor == "":
        valor=-3
  
    return valor    
       
def sanitizar_flotante(numero_str:str):
    valor = ""
    numero_str=numero_str.strip()
    
    booleano=numero_str.isalpha()
    if booleano == True:
        valor=-1
        
    if numero_str[0]== "-":
        valor=-2
        
    booleano = numero_str.isdecimal()
    if booleano == True:
        valor = float(numero_str)
        
    elif valor == "":
        valor = -3
    return valor

def sanitizar_string(valor_str:str,valor_por_defecto="-"):#valor por defecto
    valor_str=valor_str.replace("/","")
    mensaje=""
    valor_str=valor_str.strip()
    
    booleano=valor_str.isalpha()
    if booleano == True:
        mensaje=valor_str.lower()
        mensaje=mensaje.replace("/"," ")
    else:
        mensaje="N/A"
    return mensaje
  
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    tipo_dato=tipo_dato.lower()
    booleano=clave in heroe
    
    if booleano ==True:
        
        if tipo_dato == "string":
            retorno = sanitizar_string(heroe[clave])
            if retorno =="N/A":
                mensaje=False
            else:
                mensaje=True
                    
        elif tipo_dato == "flotante":
            retorno = sanitizar_flotante(heroe[clave])
                    
            if retorno >0:
                mensaje = True
            else:
                mensaje = False
                    
        elif tipo_dato == "entero":
            retorno = sanitizar_entero (heroe[clave])
            
            if retorno >0:
                mensaje = True
            else:
                mensaje = False
                
        else:
            mensaje="tipo de dato no reconocido"
    else:
        mensaje="la clave especificada no se encuentra en el heroe"  
            
    return mensaje
   
def stark_normalizar_datos(lista_heroes:list):
    
    if len(lista_heroes) > 0:
        for superheroe in lista_heroes:
            mensaje=sanitizar_dato(superheroe,"inteligencia","string")
            
        if mensaje == True:
            print("datos normalizados")
        else:
            print("no se pudo normalizar los datos")
            
    else:
        print("error la lista esta vacia")    

def generar_indice_nombres(lista_heroes):
    lista_nombres=[]
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if type(heroe) == dict:
                nombres=heroe["nombre"].split(" ")
                for palabras in nombres:
                    lista_nombres.append(palabras)
                    
            else: 
                print("el origen de datos no contiene el formato correcto")
    else:
        print("lista vacia")

    return lista_nombres

def stark_imprimir_indice_heroe(lista_heroes):
    cadena="-"
    lista=generar_indice_nombres(lista_heroes)
    nombres=cadena.join(lista)
    print(nombres)
    
def covertir_cm_a_mtrs(valor_cm:float):
    
    if type(valor_cm) == float:
        resultado=valor_cm/100
    else:
        resultado=-1
    return resultado

def generar_separador(patron:str,largo:int,imprimir=True):
    
    if len(patron) >=1 and len(patron) <3 and type(largo) == int and largo>=1 and largo <236:
        separador = patron * largo
    else:
        return "N/A"
    if imprimir == True:
        print(separador)
        return separador
    else:
        return(separador)
    
def generar_encabezado(titulo:str):
    titulo = titulo.upper()
    separador=generar_separador("*",100)
    print(titulo)
    print(separador)
    
def imprimir_ficha_heroe(heroe:dict):
    generar_encabezado("principal")
    
    print(f"         NOMBRE DEL HEROE:        {heroe['nombre']}({extraer_iniciales(heroe['nombre'])})") 
    
    print(f"         IDENTIDAD SECRETA:       {heroe['identidad']} \n")
    
    print(f"         CONSULTORA:       {heroe['empresa']} \n")
    
    print(f"         CODIGO HEROE:")        #{heroe['codigo_heroe']} \n")
    
    generar_encabezado("FISICO")
    
    print(f"         ALTURA :        {heroe['altura']} \n")
    
    print(f"         PESO:        {heroe['peso']} \n")
    
    print(f"         FUERZA:        {heroe['fuerza']} \n")
    
    generar_encabezado("SEÑAS PARTICULARES")
    
    print(f"         COLOR DE OJOS:        {heroe['color_ojos']} \n")
    
    print(f"         COLOR DE PELO:        {heroe['color_pelo']} \n")
      
def stark_navegar_fichas(lista_heroes:list):
    
    indice = 0
    
    print("""
            opcion 1: ir a la izquierda
            opcion 2: ir a la derecha
            opcion 3: salir""")
    respuesta = int(input("que opcion desea?: "))
    
    while respuesta != "s":
    
        if respuesta == 1 :
        
            if indice == 0 :
            
                indice = -1       
            
            else:
            
                indice -= 1
                
        elif(respuesta == 2):
        
            if(indice == len(lista_heroes[-1])):
            
                indice = 0
            
            else:
            
                indice += 1
        elif respuesta == 3:
            break
        
        print(imprimir_ficha_heroe(lista_heroes[indice]))    
        
        respuesta = int(input("queres otra opcion ?: "))         
 

def imprimir_menu():
    
    print("""

    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    6 - Salir""")  
    
def stark_menu_principal():
    imprimir_menu()
    
    opcion=int(input("ingrese una opcion del menu: "))
    
    return opcion
        
def stark_marvel_app_3(lista_heroes):
    
    while True : 
        
        opcion = stark_menu_principal()  
        
        if opcion == 1:
            star_imprimir_nombres_iniciales(lista_heroes)
        
        elif opcion == 2:
            pass
        
        elif opcion == 3:
            stark_normalizar_datos(lista_heroes)
            
        
        elif opcion == 4:
            stark_imprimir_indice_heroe(lista_heroes)
        
        elif opcion == 5:
            stark_navegar_fichas(lista_heroes) 
        
        elif opcion == 6:
            break
     
stark_marvel_app_3(lista_personajes)
