
def sumar(numero_uno, numero_dos):#parametros formales de la funcion
    """
    funcion que se encarga de pedir dos numeros,sumarlos y resultado
    """
    suma= numero_uno+numero_dos
        
    return suma

def restar(numero_uno,numero_dos):
    #desarollo de la funcion
    """
    funcion que se encarga de pedir dos numeros,restarlo y resultado
    """  
    resta=numero_uno - numero_dos
        
    return resta

def dividir(numero_uno,numero_dos):
    """
    funcion que se encarga de pedir dos numeros,sumarlos y resultado
    En caso de que el segundo numero sea cero va a mostrar que no
    se puede dividir por cer
    """
    division=None
        
    if numero_dos != 0:
        division=numero_uno / numero_dos
        
    return division
         
    
def multiplicar(numero_uno,numero_dos): 
    """
    funcion que se encarga de pedir dos numeros,multiplicarlo y resultado
    """
        
    multiplicacion=numero_uno * numero_dos
        
    return multiplicacion
  
def pedir_entero(mensaje):
    numero = input(f"{mensaje} :")  
    numero =int(numero)
    
    return numero

  
  
  
def mostrar_menu_principal():  
    """
    funcion que muestra el menu principal,me pide una opcion y
    me deja manipular la calculadora
    """      
    repeticion = True

    while repeticion == True:
        print ("bievenidos a la calculadora magica|n1-sumar|n2-restar|n3-dividir|n4-multiplicar|5salir")
        opcion=int(input("eliga un opcion: "))
        numero_uno=pedir_entero("ingrese un primer numero")
        numero_dos=pedir_entero("ingrese un segundo numero")

        if opcion == 1 :
            #llamada a la funcion
            resultado=sumar(numero_uno,numero_dos)#parametros actuales
            print(f"el resultado de la suma es: {resultado}")
        elif opcion == 2:
            resultado=restar(numero_uno,numero_dos)
            print(f"la resta es: {resultado}")
            
        elif opcion == 3:
            resultado = multiplicar(numero_uno,numero_dos)
            print(f"el resultado de la multiplicacion es: {resultado} ")
        elif opcion ==4:   
            division=dividir(numero_uno,numero_dos)
            if division == None:
                print("no se pudo dividir")
            else:
                print(f"el resultado de la division es:{division} ")

        elif opcion == 5:
            repeticion=False
mostrar_menu_principal() 