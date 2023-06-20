
'''archivo_sin_leer = open("nombres.txt","r")'''
#leer archivo complet0

'''archivo= archivo_sin_leer.read()'''
#leer el archivo linea por linea
'''archivo = archivo_sin_leer.readlines()'''

#LEER UNA LINEA

'''linea = archivo_sin_leer.readline(1)'''
# cerrar el archivo

'''archivo_sin_leer.close()'''

#print(linea)


# abriendo el archivo con with para leerlo
'''with open("nombres.txt","r") as archivo:'''
    #mostramos el contenido

with open("nombres.txt","w") as archivo:
    # sobreescribir un archivo
    #archivo.write()
    
    #agregando dos lineas
    archivo.writelines(["te reeiscribi todo\n","todo bien"])




