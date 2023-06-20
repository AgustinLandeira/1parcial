
#La división de higiene está trabajando en un control de stock para productos
#sanitarios. Debemos realizar la carga de
#una compra de productos de prevención de contagio, de cada una debe obtener los
#siguientes datos:
#· El tipo (&quot;barbijo&quot;, &quot;jabón&quot; o &quot;alcohol&quot;)
#· El precio
#· La cantidad de unidades
#· La marca
#· El fabricante
#Se debe informar los datos de la compra procesados para poder iniciar el control de
#stock.

#system("clm")
 #from os import system




tipo=input("el tipo de producto es: ")

while(tipo !="jabon" and tipo!="alcohol" and tipo !="barbijo"):
    tipo=input("ERROR porfavor ingrese jabon, alcohol o barbijo: ")
    

precio= float (input("ingrese el precio de producto: "))

cantidad_unidades=  int (input("ingrese la cantidad de unidades: "))


marca=input("ingrese la marca: ")

fabricante=input("ingrese el nombre del fabricante: ")

print("el tipo de producto es:{0}" .format(tipo))
print("el precio es: {0}".format(precio))
print("la cantidad de unidades en total es: {0} ".format(cantidad_unidades))
print("la marca es: {0} ".format(marca))
print("el fabricante se llama: {0}".format(fabricante))