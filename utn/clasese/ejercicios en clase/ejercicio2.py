#Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
#python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
#al ingresar el número debemos mostrarle que regla de estilo representa y su
#descripción (Sacar la información de las diapositivas de las reglas de estilo).
#En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
#“Error, regla de estilo inexistente”

numero_ingresado=input("ingrese un numero entre el 1 y 8: ")

if numero_ingresado == "1":
    print("""¿cual es el sentido?  no solo es importante escribir código que no sólo funcione, 
    sino que además pueda ser leído con facilidad.""")
else:
    if numero_ingresado=="2" :
        print(""" ¿que es pep?
            es un documentoque proporciona información a la comunidad de
            Python, o que describe una nueva característica.""")
    else:
        if numero_ingresado == "3":
            print(""" ¿que es pep8?
            Es un conjunto de recomendaciones cuyo objetivo
            es ayudar a escribir código más legible y abarca
            desde cómo nombrar variables, al número máximo
            de caracteres que una línea debe tener. """)
        else:
            if numero_ingresado == "4":
                print(""" identado:
                Python no usa {} para designar bloques de código
                como otros lenguajes de programación, sino que
                usa bloques identados para indicar que un
                determinado bloque de código pertenece a por
                ejemplo un if.  """)
            else:
                if numero_ingresado == "5":
                    print(""" tamaño maximo linea:
                    Se recomienda limitar el tamaño de cada línea a
                    79 caracteres, para evitar tener que hacer scroll a
                    la derecha.      """)
                    
                else:
                    if numero_ingresado == "6":
                        print("""lineas en blanco:
                        El uso de espacios en blanco mejora la legibilidad
                        del código, y es por lo que la PEP8 indica dónde
                        debemos usar espacios y dónde no.""")
                    else:
                        if numero_ingresado =="7":
                            print("""comentarios : 
                            Cualquier comentario que contradiga el código es
                            peor que ningún comentario y o si actiualizamos el codigo
                            tambien los comentarios.""")
                        else:
                            if numero_ingresado =="8":
                                print(""" nombres : 
                                Funciones: Uso de snake_case, letras en
                                minúscula separadas por guión bajo: mi_funcion.

                                Variables: Al igual que las funciones: variable,
                                mi_variable.

                                Clases: Uso de CamelCase, usando mayúscula y
                                sin barra baja: MiClase, ClaseDePrueba.      """)
                            else:
                                print("el numero que elegiste no esta en el rango")
                        
                    